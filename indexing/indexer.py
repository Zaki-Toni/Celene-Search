import os
import logging
from whoosh.index import create_in, open_dir, exists_in
from whoosh.fields import Schema
from whoosh.writing import IndexWriter
from whoosh.filedb.filestore import FileStorage

from .document import Document

# Configuración básica de logging para este módulo
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class Indexer:
    """
    Gestiona la creación y escritura del índice invertido utilizando Whoosh.

    Esta clase implementa una estrategia de 'solo adición' (append-only), donde
    los documentos no se actualizan, sino que se agregan nuevas versiones.
    Es responsable de inicializar el almacenamiento del índice si no existe.
    """

    def __init__(self, index_path, schema):
        """
        Inicializa el Indexer, asegurando que el directorio y el índice existan.

        Si el directorio especificado no existe, lo crea.
        Si el índice no existe dentro del directorio, lo inicializa con el esquema dado.
        Si ya existe, simplemente lo carga para su uso.
        """
        self.index_path = index_path
        self.schema = schema
        self.ix = self._initialize_index()

    def _initialize_index(self):
        """
        Lógica interna para abrir o crear el índice de manera segura.
        """
        try:
            # 1. Verificar y crear el directorio si es necesario
            if not os.path.exists(self.index_path):
                logger.info(f"El directorio de índice '{self.index_path}' no existe. Creándolo...")
                os.makedirs(self.index_path)

            # 2. Verificar si ya existe un índice de Whoosh en ese directorio
            if exists_in(self.index_path):
                logger.info(f"Índice encontrado en '{self.index_path}'. Abriendo...")
                return open_dir(self.index_path)
            else:
                logger.info(f"No se encontró un índice en '{self.index_path}'. Creando uno nuevo...")
                return create_in(self.index_path, self.schema)

        except OSError as e:
            logger.critical(f"Error crítico del sistema de archivos al inicializar el índice: {e}")
            raise

    def add_documents(self, documents):
        """
        Agrega una lista de objetos Document al índice en un solo lote (batch).

        Maneja errores individuales por documento para evitar detener todo el proceso.
        """
        if not documents:
            logger.warning("Se llamó a add_documents con una lista vacía.")
            return 0

        success_count = 0
        logger.info(f"Iniciando indexación de {len(documents)} documentos...")

        try:
            writer = self.ix.writer(limitmb=512)

            with writer:
                for doc in documents:
                    try:
                        # Convertimos el documento al dict que espera Whoosh
                        doc_data = doc.to_indexable()

                        # Añadimos al índice
                        writer.add_document(**doc_data)

                        success_count += 1

                    except ValueError as ve:
                        logger.error(
                            f"Error de validación de datos para el documento "
                            f"{getattr(doc, 'id', 'DESCONOCIDO')}: {ve}"
                        )

                    except Exception as e:
                        logger.error(
                            f"Error inesperado al procesar el documento "
                            f"{getattr(doc, 'id', 'DESCONOCIDO')}: {e}"
                        )

            logger.info(f"Lote finalizado. Indexados exitosamente: {success_count}/{len(documents)}")

        except Exception as e:
            logger.critical(f"Error fatal en el proceso de escritura por lotes (IndexWriter): {e}")
            return 0

        return success_count
