from dataclasses import dataclass
from .arbol import Arbol

@dataclass
class Olivo(Arbol):
    tipo_aceituna: str = "Arbequina"

    def absorber(self, litros: float) -> None:
        super().absorber(litros)
        # regla: +0.01 m por riego
        if litros > 0:
            self.altura_m += 0.01
