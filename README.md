# Celene-Search
Indexación y recuperación de la información

# 🔍 Motor de Búsqueda Inteligente: Expansión de Consultas

## Descripción del Proyecto

Este proyecto implementa un **Motor de Búsqueda Inteligente** que supera las limitaciones de la búsqueda por coincidencia exacta de términos. Utilizando técnicas de Procesamiento del Lenguaje Natural (**NLP**) y recursos léxicos, el sistema es capaz de **expandir automáticamente** las consultas del usuario con sinónimos, aumentando significativamente la **relevancia** y la **recuperación** de información.

El núcleo del sistema simula un módulo de consulta avanzado de Lucene/Whoosh, incorporando WordNet y POS Tagging para un pre-procesamiento contextual de la búsqueda.

---

## Características Principales

* **Expansión de Consultas:** Uso de **NLTK WordNet** para encontrar sinónimos y lemas para los términos clave de la consulta.
* **Pre-procesamiento Lingüístico:**
    * Eliminación de palabras vacías para enfocar la expansión solo en los términos relevantes.
    * Etiquetado Gramatical: Permite buscar sinónimos específicos según el contexto de la palabra (ej: buscar sinónimos de 'banco' como sustantivo).
* **Motor de Búsqueda Robusto:** Implementación de indexación y recuperación con la librería **Whoosh**.
* **Interfaz Web:** Servidor ligero implementado con **???** para una interacción simple y visualización de resultados.

---

## 🏗️ Arquitectura del Sistema

El proyecto sigue una arquitectura modular en capas, garantizando la separación de responsabilidades:

1.  **Capa de Presentación (`WebController`):** Maneja las peticiones HTTP y la interfaz de usuario (???).
2.  **Capa de Servicio (`QueryExpander`):** Contiene la lógica de negocio y NLP.
3.  **Capa de Datos (`IndexManager`/`SearchEngine`):** Administra el índice de Whoosh.

El flujo de una búsqueda es: `Consulta de Usuario (String) -> QueryExpander (Expansión y Booleano) -> Whoosh (Búsqueda) -> Resultados`.



---

## 🛠️ Tecnologías Utilizadas

| Componente | Herramienta | Función |
| :--- | :--- | :--- |
| **Búsqueda/Indexación** | `whoosh` | Motor de búsqueda principal (análogo a Lucene). |
| **NLP** | `nltk` | Herramientas para tokenización, stop-words, y POS Tagging. |
| **Recurso Léxico** | `nltk.corpus.wordnet` | Fuente de sinónimos para la expansión. |
| **Interfaz Web** | `???` | Framework para el servidor web y la interfaz de búsqueda. |
| **Lenguaje** | `Python 3.x` | Lenguaje de programación principal. |

---
