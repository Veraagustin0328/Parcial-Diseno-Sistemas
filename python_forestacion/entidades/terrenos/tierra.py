from dataclasses import dataclass, field
from typing import Optional
from .plantacion import Plantacion

@dataclass
class Tierra:
    padron: int
    superficie_total_m2: float
    domicilio: str
    _plantacion: Optional[Plantacion] = field(default=None, repr=False)

    def asignar_plantacion(self, plantacion: "Plantacion") -> None:
        self._plantacion = plantacion

    def get_finca(self) -> "Plantacion":
        if self._plantacion is None:
            raise ValueError("La tierra no tiene plantación asignada.")
        return self._plantacion
