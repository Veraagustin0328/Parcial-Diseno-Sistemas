from dataclasses import dataclass
from .cultivo import Cultivo

@dataclass
class Hortaliza(Cultivo):
    estado: str = "semilla"  # estado simple para ejemplo

    def absorber(self, litros: float) -> None:
        if litros <= 0:
            return
        self.agua_acumulada_l += litros
