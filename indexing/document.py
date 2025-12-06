from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar

@dataclass(frozen=True)
class Document:
    """
    Representa una unidad de información inmutable, lista para ser indexada.
    """

    # 1. CAMPOS REQUERIDOS
    id: str = field(metadata={'required': True})
    title: str = field(metadata={'required': True})
    content: str = field(metadata={'required': True})

    # 2. METADATOS CRÍTICOS
    source_url: str | None = field(default=None)
    author: str | None = field(default=None)

    # 3. CAMPO CLAVE PARA EL RANKING POR FRESCURA
    timestamp: datetime = field(default_factory=datetime.now)

    # 4. CONSTANTES DE CLASE (Ignoradas por dataclass)
    # Definimos los campos que Whoosh espera en el método to_indexable
    _WHOOSH_FIELDS: ClassVar[list[str]] = ['doc_id', 'title', 'content', 'url', 'author', 'timestamp']

    def to_indexable(self) -> dict:
        """
        Convierte la instancia de Documento en un diccionario de campos
        compatible con el proceso de indexación de Whoosh.
        """

        indexable_data = {
            'doc_id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp,
        }

        indexable_data['url'] = self.source_url if self.source_url is not None else ""
        indexable_data['author'] = self.author if self.author is not None else ""

        return indexable_data
