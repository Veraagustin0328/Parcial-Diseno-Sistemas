from dataclasses import dataclass
from .cultivo import Cultivo

@dataclass
class Arbol(Cultivo):
    altura_m: float = 0.0  # árboles crecen por riego

    def absorber(self, litros: float) -> None:
        if litros <= 0:
            return
        self.agua_acumulada_l += litros
