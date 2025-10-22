from dataclasses import dataclass
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.arbol import Arbol

@dataclass
class ArbolService(CultivoService):
    def post_riego(self, cultivo: Arbol, litros: float) -> None:
        if litros > 0:
            cultivo.altura_m += 0.01
