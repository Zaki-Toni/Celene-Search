from whoosh.fields import Schema, ID, TEXT, DATETIME, KEYWORD
from whoosh.analysis import StandardAnalyzer
from whoosh.lang.spanish import find_stopwords

class DocumentSchema:
    """
    Define el esquema de Whoosh para el índice del motor de búsqueda Celene-Search.

    Esta implementación utiliza el analizador estándar de Whoosh, configurado
    con las listas de palabras vacías (stopwords) del español, como punto de
    partida para la indexación funcional.
    """
    @staticmethod
    def create_schema() -> Schema:
        """
        Devuelve el objeto Schema listo para inicializar el índice de Whoosh.

        :returns: Objeto Schema con la definición de campos.
        :rtype: whoosh.fields.Schema
        """
        # 1. CONFIGURACIÓN DEL ANALIZADOR BÁSICO. DEBEMOS CREAR UN ANALIZADOR MAS COMPLEJO
        # Usamos StandardAnalyzer, que aplica tokenización y minúsculas.
        # Le proporcionamos la lista de stopwords del español para filtrado.
        spanish_analyzer = StandardAnalyzer(
            stoplist=find_stopwords(),
            minsize=2  # Filtra tokens de 1 carácter
        )

        return Schema(
            # ID (Clave Primaria): Almacenado y buscable, sin análisis.
            doc_id=ID(stored=True, unique=True),

            # TITLE: Buscable, analizado, con impulso (boost) para aumentar relevancia.
            title=TEXT(analyzer=spanish_analyzer, stored=False, field_boost=2.0),

            # CONTENT (Búsqueda Principal): Analizado y almacenado para snippets.
            content=TEXT(analyzer=spanish_analyzer, stored=True),

            # TIMESTAMP: Campo de fecha/hora, almacenado y ordenable para ranking por frescura.
            timestamp=DATETIME(stored=True, sortable=True),

            # AUTHOR y URL (Metadatos): KEYWORD para filtrado exacto y eficiente.
            author=KEYWORD(stored=True, lowercase=True, scorable=True),
            url=KEYWORD(stored=True, lowercase=True)
        )
