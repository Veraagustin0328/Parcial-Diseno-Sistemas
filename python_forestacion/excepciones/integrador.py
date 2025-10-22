"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\excepciones
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\excepciones\__init__.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
from .superficie_insuficiente_exception import SuperficieInsuficienteException
from .agua_agotada_exception import AguaAgotadaException
from .persistencia_exception import PersistenciaException

__all__ = [
    "ForestacionException",
    "SuperficieInsuficienteException",
    "AguaAgotadaException",
    "PersistenciaException",
]


# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\excepciones\agua_agotada_exception.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
class AguaAgotadaException(ForestacionException):
    """No hay agua suficiente para realizar la operacion."""
    pass


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\excepciones\forestacion_exception.py
# ================================================================================

﻿class ForestacionException(Exception):
    """Excepcion base del dominio Forestacion."""
    pass


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\excepciones\mensajes_exception.py
# ================================================================================

﻿MSJ_SUPERFICIE_INSUFICIENTE = "Superficie insuficiente para plantar."
MSJ_AGUA_AGOTADA           = "No hay agua suficiente en la plantacion."
MSJ_LITROS_INVALIDOS       = "Los litros de riego deben ser > 0."


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\excepciones\persistencia_exception.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
class PersistenciaException(ForestacionException):
    """Error de lectura/escritura en persistencia."""
    pass


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
class SuperficieInsuficienteException(ForestacionException):
    """Se intenta plantar superando la superficie disponible."""
    pass


