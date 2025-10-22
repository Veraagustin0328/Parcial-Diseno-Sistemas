from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Cultivo(ABC):
    nombre: str
    superficie_m2: float
    agua_acumulada_l: float = 0.0

    @abstractmethod
    def absorber(self, litros: float) -> None:
        """Cada cultivo define cómo “consume/absorbe” agua al regar."""
        raise NotImplementedError
