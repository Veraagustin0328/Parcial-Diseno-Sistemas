from dataclasses import dataclass
from .hortaliza import Hortaliza

@dataclass
class Lechuga(Hortaliza):
    variedad: str = "Crespa"

    def absorber(self, litros: float) -> None:
        # hortalizas: absorción constante (1–2L típicamente, lo maneja el servicio)
        super().absorber(litros)
