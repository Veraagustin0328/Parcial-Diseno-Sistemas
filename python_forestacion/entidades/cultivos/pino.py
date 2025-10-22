from dataclasses import dataclass
from .arbol import Arbol

@dataclass
class Pino(Arbol):
    variedad: str = "Parana"

    def absorber(self, litros: float) -> None:
        super().absorber(litros)
        # regla de crecimiento, +0.10 m por riego
        if litros > 0:
            self.altura_m += 0.10
