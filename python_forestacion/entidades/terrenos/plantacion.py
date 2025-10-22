from dataclasses import dataclass, field
from typing import List
from ..cultivos.cultivo import Cultivo

@dataclass
class Plantacion:
    nombre: str
    superficie_disponible_m2: float
    agua_disponible_l: float
    cultivos: List[Cultivo] = field(default_factory=list)

    def agregar_cultivo(self, cultivo: Cultivo) -> None:
        self.cultivos.append(cultivo)
        self.superficie_disponible_m2 -= cultivo.superficie_m2
