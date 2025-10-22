from dataclasses import dataclass
from typing import Optional
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class TierraService:
    def asignar_plantacion(self, tierra: Tierra, plantacion: Plantacion) -> None:
        """Asigna una plantacion a la tierra (reemplaza si ya hubiera)."""
        tierra.plantacion = plantacion

    def get_plantacion(self, tierra: Tierra) -> Optional[Plantacion]:
        """Devuelve la plantacion o None si no hay."""
        return tierra.plantacion
