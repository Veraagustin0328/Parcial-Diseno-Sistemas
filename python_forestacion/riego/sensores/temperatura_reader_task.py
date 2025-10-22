from dataclasses import dataclass
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

@dataclass
class TemperaturaReaderTask(Observable[EventoSensor]):
    def __init__(self) -> None:
        super().__init__()
    def emular(self, temp: float) -> None:
        self.notify(EventoSensor(tipo="temp", valor=temp))
