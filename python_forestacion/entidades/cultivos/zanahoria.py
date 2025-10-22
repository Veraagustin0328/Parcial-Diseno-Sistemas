from dataclasses import dataclass
from .hortaliza import Hortaliza

@dataclass
class Zanahoria(Hortaliza):
    baby: bool = False

    def absorber(self, litros: float) -> None:
        super().absorber(litros)
