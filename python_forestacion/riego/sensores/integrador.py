"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\riego\sensores
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\riego\sensores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\riego\sensores\humedad_reader_task.py
# ================================================================================

﻿from dataclasses import dataclass
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

@dataclass
class HumedadReaderTask(Observable[EventoSensor]):
    def __init__(self) -> None:
        super().__init__()
    def emular(self, hum: float) -> None:
        self.notify(EventoSensor(tipo="hum", valor=hum))


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\riego\sensores\temperatura_reader_task.py
# ================================================================================

﻿from dataclasses import dataclass
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

@dataclass
class TemperaturaReaderTask(Observable[EventoSensor]):
    def __init__(self) -> None:
        super().__init__()
    def emular(self, temp: float) -> None:
        self.notify(EventoSensor(tipo="temp", valor=temp))


