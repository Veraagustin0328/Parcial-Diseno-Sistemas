from dataclasses import dataclass
from typing import Type, List, TypeVar

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.excepciones import (
    SuperficieInsuficienteException,
    AguaAgotadaException,
)
from python_forestacion.excepciones.mensajes_exception import (
    MSJ_SUPERFICIE_INSUFICIENTE,
    MSJ_AGUA_AGOTADA,
    MSJ_LITROS_INVALIDOS,
)

T = TypeVar("T", bound=Cultivo)

@dataclass
class PlantacionService:
    def plantar(self, plantacion: Plantacion, cultivo: Cultivo) -> None:
        if cultivo.superficie_m2 > plantacion.superficie_disponible_m2:
            raise SuperficieInsuficienteException(MSJ_SUPERFICIE_INSUFICIENTE)
        plantacion.agregar_cultivo(cultivo)

    def regar(self, plantacion: Plantacion, cultivo: Cultivo, litros: float) -> None:
        if litros <= 0:
            raise ValueError(MSJ_LITROS_INVALIDOS)
        if plantacion.agua_disponible_l < litros:
            raise AguaAgotadaException(MSJ_AGUA_AGOTADA)
        plantacion.agua_disponible_l -= litros
        cultivo.absorber(litros)

    def cosechar_por_tipo(self, plantacion: Plantacion, tipo: Type[T]) -> List[T]:
        return [c for c in plantacion.cultivos if isinstance(c, tipo)]
