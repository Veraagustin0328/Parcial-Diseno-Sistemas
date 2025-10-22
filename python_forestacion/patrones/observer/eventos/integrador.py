"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer\eventos
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer\eventos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer\eventos\evento_plantacion.py
# ================================================================================

﻿from dataclasses import dataclass

@dataclass
class EventoPlantacion:
    mensaje: str


# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\observer\eventos\evento_sensor.py
# ================================================================================

﻿from dataclasses import dataclass

@dataclass
class EventoSensor:
    tipo: str
    valor: float


