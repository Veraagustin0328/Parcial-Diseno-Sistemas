from dataclasses import dataclass, field
from typing import Optional
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUM_MAX_RIEGO
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

@dataclass
class ControlRiegoTask:
    litros_por_cultivo: float = 1.0
    _ultima_temp: Optional[float] = field(default=None, init=False, repr=False)
    _ultima_hum: Optional[float] = field(default=None, init=False, repr=False)

    def update(self, event: EventoSensor) -> None:
        if event.tipo == "temp":
            self._ultima_temp = event.valor
        elif event.tipo == "hum":
            self._ultima_hum = event.valor

    def condiciones_ok(self) -> bool:
        if self._ultima_temp is None or self._ultima_hum is None:
            return False
        return (TEMP_MIN_RIEGO <= self._ultima_temp <= TEMP_MAX_RIEGO) and (self._ultima_hum < HUM_MAX_RIEGO)

    def evaluar_y_regar(self, plantacion: Plantacion) -> bool:
        if not self.condiciones_ok():
            return False
        svc = PlantacionService()
        rego = False
        for c in list(plantacion.cultivos):
            if plantacion.agua_disponible_l >= self.litros_por_cultivo:
                svc.regar(plantacion, c, self.litros_por_cultivo)
                rego = True
            else:
                break
        return rego
