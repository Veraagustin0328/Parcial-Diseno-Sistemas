from dataclasses import dataclass
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.lechuga import Lechuga

@dataclass
class LechugaService(CultivoService):
    def post_riego(self, cultivo: Lechuga, litros: float) -> None:
        # lechuga cambia estado simple si recibe riego
        if litros > 0 and cultivo.estado == "semilla":
            cultivo.estado = "creciendo"
