"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\factory
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\factory\cultivo_factory.py
# ================================================================================

﻿from typing import Type
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
_MAP: dict[str, Type[Cultivo]] = {"pino": Pino,"lechuga": Lechuga,"olivo": Olivo,"zanahoria": Zanahoria}
def crear_cultivo(tipo: str, **kwargs) -> Cultivo:
    cls = _MAP.get(tipo.lower())
    if cls is None:
        raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
    return cls(**kwargs)


