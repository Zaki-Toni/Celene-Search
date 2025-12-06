from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class Document:
    """
    Representa una unidad de información inmutable, lista para ser indexada.
    """

    # 1. CAMPOS REQUERIDOS
    id = field(metadata={'required': True})
    title = field(metadata={'required': True})
    content = field(metadata={'required': True})

    # 2. METADATOS CRÍTICOS
    source_url = field(default=None)
    author = field(default=None)

    # 3. CAMPO CLAVE PARA EL RANKING POR FRESCURA
    timestamp = field(default_factory=datetime.now)

    # 4. CONSTANTES DE CLASE
    _WHOOSH_FIELDS = ['doc_id', 'title', 'content', 'url', 'author', 'timestamp']

    def to_indexable(self):
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
