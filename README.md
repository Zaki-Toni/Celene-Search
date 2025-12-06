# 🔍 Celene-Search: Motor de Búsqueda Inteligente (Query Expansion)
## Indexación y Recuperación de la Información

## Descripción del Proyecto

Este proyecto implementa un **Motor de Búsqueda Inteligente** que supera las limitaciones de la búsqueda por coincidencia exacta. Utilizando técnicas de **Procesamiento del Lenguaje Natural (NLP)** y recursos léxicos **(WordNet)**, el sistema es capaz de **expandir automáticamente** las consultas del usuario con sinónimos, aumentando significativamente la **relevancia** y la **recuperación** de información.

El núcleo del sistema simula un módulo de consulta avanzado, utilizando la librería **Whoosh** para la indexación y una arquitectura modular estricta para el pre-procesamiento contextual.

---

## Características y Ventajas

* **Expansión Contextual:** Uso de **NLTK WordNet** y **Etiquetado Gramatical (POS Tagging)** para buscar sinónimos de los términos clave según su función sintáctica (ej: "banco" como sustantivo vs. "banco" como verbo).
* **Pipeline de PLN Modular:** Proceso de consulta estructurado en componentes atómicos (`Tokenizer`, `StopwordFilter`, `POSTagger`) para facilitar el mantenimiento y la sustitución.
* **Motor de Búsqueda Robusto:** Implementación de indexación y recuperación eficiente con la librería **Whoosh**.
* **Arquitectura Desacoplada:** Uso de interfaces explícitas para separar las responsabilidades de Búsqueda e Indexación.

---

## 🏗️ Arquitectura del Sistema (Basada en Componentes UML)

El proyecto sigue una arquitectura modular en capas, garantizando la separación de responsabilidades y la **inversión de dependencias** mediante el uso de interfaces.

### 1. Estructura Lógica

El sistema se divide en cuatro componentes principales con responsabilidades claras:

| Componente | Rol Principal | Interfaz Clave |
| :--- | :--- | :--- |
| **`Web Interface`** | Gestiona la presentación y las peticiones HTTP (Capa de Presentación). | - |
| **`Search Components`** | Orquestador de la lógica de negocio; utiliza el PLN y requiere acceso al índice (Capa de Servicio). | **Requiere `IIndexAccess`** |
| **`NLP Components`** | Procesa y mejora la consulta del usuario (Lógica de Expansión). | - |
| **`Indexing Components`** | Gestiona la carga y la creación del índice físico (Capa de Datos). | **Provee `IIndexAccess`** |

### 2. Flujo de Búsqueda (`SearchEngine`)

El **`SearchEngine`** orquesta el proceso siguiendo estos pasos:

1.  **Recepción:** Recibe la consulta del `???? App`.
2.  **Expansión:** Llama al **`QueryExpander`** para ejecutar el pipeline de PLN.
3.  **Búsqueda:** Utiliza la interfaz **`IIndexAccess`** (provista por el `Whoosh Index`) para ejecutar la búsqueda con la consulta expandida.
4.  **Entrega:** Formatea los resultados (`SearchResult`) y los devuelve a la interfaz web.

---

## 🛠️ Tecnologías Utilizadas

| Componente | Herramienta | Función |
| :--- | :--- | :--- |
| **Búsqueda/Indexación** | `whoosh` | Motor de búsqueda principal y base para la interfaz `IIndexAccess`. |
| **Web Interface** | **`????`** | Framework ligero de Python para el servidor web y la interfaz de búsqueda. |
| **NLP Pipeline** | `nltk` | Herramientas para tokenización, stop-words, y POS Tagging. |
| **Recurso Léxico** | `nltk.corpus.wordnet` | Fuente de sinónimos para la expansión. |
| **Lenguaje** | `Python 3.x` | Lenguaje de programación principal. |

---
