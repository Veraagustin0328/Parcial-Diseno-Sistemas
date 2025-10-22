from dataclasses import dataclass
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

@dataclass
class HumedadReaderTask(Observable[EventoSensor]):
    def __init__(self) -> None:
        super().__init__()
    def emular(self, hum: float) -> None:
        self.notify(EventoSensor(tipo="hum", valor=hum))
