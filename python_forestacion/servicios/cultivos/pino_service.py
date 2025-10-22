from dataclasses import dataclass
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.entidades.cultivos.pino import Pino

@dataclass
class PinoService(ArbolService):
    def post_riego(self, cultivo: Pino, litros: float) -> None:
        # pino crece más por riego
        cultivo.altura_m += 0.10 if litros > 0 else 0.0
