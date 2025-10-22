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
