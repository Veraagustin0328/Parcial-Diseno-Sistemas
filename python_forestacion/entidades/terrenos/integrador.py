"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\terrenos
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\terrenos\plantacion.py
# ================================================================================

from dataclasses import dataclass, field
from typing import List
from ..cultivos.cultivo import Cultivo

@dataclass
class Plantacion:
    nombre: str
    superficie_disponible_m2: float
    agua_disponible_l: float
    cultivos: List[Cultivo] = field(default_factory=list)

    def agregar_cultivo(self, cultivo: Cultivo) -> None:
        self.cultivos.append(cultivo)
        self.superficie_disponible_m2 -= cultivo.superficie_m2


# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\terrenos\registro_forestal.py
# ================================================================================

from dataclasses import dataclass, field
from typing import List
from python_forestacion.entidades.terrenos.tierra import Tierra

@dataclass
class RegistroForestal:
    nombre: str
    tierras: List[Tierra] = field(default_factory=list)

    def alta_tierra(self, tierra: Tierra) -> None:
        """Agrega una tierra al registro."""
        self.tierras.append(tierra)


# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\terrenos\tierra.py
# ================================================================================

﻿from dataclasses import dataclass
from typing import Optional
from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class Tierra:
    padron: int
    superficie_total_m2: float
    domicilio: str
    plantacion: Optional[Plantacion] = None


