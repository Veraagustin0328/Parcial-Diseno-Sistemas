"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer\observable.py
# ================================================================================

from typing import Generic, List, TypeVar
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

class Observable(Generic[T]):
    def __init__(self) -> None:
        self._observers: List[Observer[T]] = []

    def attach(self, observer: Observer[T]) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer[T]) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event: T) -> None:
        for obs in self._observers:
            obs.update(event)


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer\observer.py
# ================================================================================

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

class Observer(ABC, Generic[T]):
    @abstractmethod
    def update(self, event: T) -> None:
        pass


