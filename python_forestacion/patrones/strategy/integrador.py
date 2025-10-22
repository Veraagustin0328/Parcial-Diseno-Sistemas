"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\strategy
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\strategy\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ================================================================================

﻿from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz Strategy: define como un cultivo absorbe agua."""
    @abstractmethod
    def absorber(self, cultivo: Cultivo, litros: float) -> None:
        pass


