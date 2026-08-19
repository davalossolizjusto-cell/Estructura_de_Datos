# 🚀 Prácticas y Laboratorios · Estructuras de Datos 1

<p align="center">
  <b>Repositorio oficial para el desarrollo, control de calidad y buenas prácticas de codificación en Python.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PEP%208-Compliant-success?style=for-the-badge&logo=python&logoColor=white" alt="PEP 8">
  <img src="https://img.shields.io/badge/Status-En%20Desarrollo-orange?style=for-the-badge" alt="Status">
</p>

---

## 📋 Tabla de Contenidos
1. [🎯 Enfoque y Calidad de Código](#-enfoque-y-calidad-de-código)
2. [📏 Aplicación de PEP 8 (Ejemplo Práctico)](#-aplicación-de-pep-8-ejemplo-práctico)
3. [📂 Estructura del Repositorio](#-estructura-del-repositorio)
4. [🧪 Proceso de Pruebas y Validación](#-proceso-de-pruebas-y-validación)
5. [📈 Registro de Avance de Prácticas](#-registro-de-avance-de-prácticas)

---

## 🎯 Enfoque y Calidad de Código

Cada ejercicio y práctica en este repositorio no solo busca resolver un problema algorítmico, sino también cumplir con estándares de nivel profesional de la industria:
* **Legibilidad:** Código limpio, auto-documentado y estructurado lógicamente.
* **Tipado Estático:** Uso de `Type Hints` en funciones y métodos públicos.
* **Documentación:** Docstrings formales siguiendo el estándar de Python.
* **Robustez:** Manejo de excepciones personalizadas en lugar de errores genéricos o impresiones por consola.

---

## 📏 Aplicación de PEP 8 (Ejemplo Práctico)

A continuación se muestra una comparativa de cómo se refactoriza un script común para cumplir con la guía de estilo oficial **PEP 8**:

### ❌ Código Incorrecto (Antipatrones)
```python
# Mal uso de nombres, sin espacios, sin tipado y sin docstrings
class milonodo:
    def __init__(self,D):
        self.val=D
        self.sig=None

def INS_DATOS(self,val):
    temp=milonodo(val)
    temp.sig=self.cabeza
    self.cabeza=temp        
```

### ✅ Código Correcto y Limpio (PEP 8 Compliant)

```
from typing import Any, Optional

class ListaEnlazada:
    """
    Implementación base que cumple estrictamente con PEP 8, 
    Type Hints y documentación formal.
    """

    class _Nodo:
        """Estructura interna para almacenar un nodo y su enlace."""
        def __init__(self, dato: Any) -> None:
            self.dato: Any = dato
            self.siguiente: Optional['ListaEnlazada._Nodo'] = None

    def __init__(self) -> None:
        self._cabeza: Optional[ListaEnlazada._Nodo] = None
        self._tamanio: int = 0

    def insertar_al_inicio(self, dato: Any) -> None:
        """
        Inserta un nuevo elemento al inicio de la lista enlazada.

        Args:
            dato: El valor de cualquier tipo a almacenar.
        """
        nuevo_nodo = self._Nodo(dato)
        nuevo_nodo.siguiente = self._cabeza
        self._cabeza = nuevo_nodo
        self._tamanio += 1
 ```
## 📂 Estructura del Repositorio
La organización de carpetas separa la lógica de las estructuras, las pruebas unitarias y los scripts de ejecución:
```
estudio_estructuras/
├── README.md
├── estructuras/
│   ├── __init__.py
│   ├── excepciones.py       ← Errores personalizados
│   ├── pila.py              ← Práctica 1: Pilas
│   └── cola.py              ← Práctica 2: Colas
├── tests/
│   ├── __init__.py
│   ├── test_pila.py         ← Pruebas unitarias (Pytest / Unittest)
│   └── test_cola.py
└── main.py                  ← Script principal de demostración
```
## 🧪 Proceso de Pruebas y Validación
Antes de dar por finalizada cualquier práctica, el código pasa por un flujo de validación automática:

Linting de Estilo: Verificación de formato con herramientas como flake8 o black.

Ejecución de Pruebas Unitarias: Se validan casos borde (estructuras vacías, desbordamientos, tipos de datos nulos).
```
python -m unittest discover -s tests
```
---
## 📈 Registro de Avance de Prácticas


|Práctica / Módulo|Estado|Cumplimiento PEP8|Pruebas Unitarias|Fecha de Revisión|
|-----------------|------|-----------------|-----------------|-----------------|
|00Estándares y PEP 8|🟢Completado|✅100%✅|Aprobadas|Semana 1|
|Pilas y Colas|🟢Completado|✅100%|✅Aprobadas|Semana 2|
|Listas Enlazadas|🟢Completado|✅100%|✅Aprobadas|Semana 4|
|Árboles Binarios|🟡En proceso|🔄En revisión❌|Pendientes|Semana7| 
|Tablas Hash|-|-|🔴Pendiente——|Semana 10|




