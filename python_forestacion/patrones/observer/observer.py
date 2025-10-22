from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

class Observer(ABC, Generic[T]):
    @abstractmethod
    def update(self, event: T) -> None:
        pass
