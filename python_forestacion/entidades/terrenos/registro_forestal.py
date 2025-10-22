from dataclasses import dataclass, field
from typing import List
from python_forestacion.entidades.terrenos.tierra import Tierra

@dataclass
class RegistroForestal:
    nombre: str
    tierras: List[Tierra] = field(default_factory=list)

    def alta_tierra(self, tierra: Tierra) -> None:
        """Agrega una tierra al registro."""
        self.tierras.append(tierra)
