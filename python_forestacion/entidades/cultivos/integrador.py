"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\arbol.py
# ================================================================================

from dataclasses import dataclass
from .cultivo import Cultivo

@dataclass
class Arbol(Cultivo):
    altura_m: float = 0.0  # árboles crecen por riego

    def absorber(self, litros: float) -> None:
        if litros <= 0:
            return
        self.agua_acumulada_l += litros


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Cultivo(ABC):
    nombre: str
    superficie_m2: float
    agua_acumulada_l: float = 0.0

    @abstractmethod
    def absorber(self, litros: float) -> None:
        """Cada cultivo define cómo “consume/absorbe” agua al regar."""
        raise NotImplementedError


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\hortaliza.py
# ================================================================================

from dataclasses import dataclass
from .cultivo import Cultivo

@dataclass
class Hortaliza(Cultivo):
    estado: str = "semilla"  # estado simple para ejemplo

    def absorber(self, litros: float) -> None:
        if litros <= 0:
            return
        self.agua_acumulada_l += litros


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

from dataclasses import dataclass
from .hortaliza import Hortaliza

@dataclass
class Lechuga(Hortaliza):
    variedad: str = "Crespa"

    def absorber(self, litros: float) -> None:
        # hortalizas: absorción constante (1–2L típicamente, lo maneja el servicio)
        super().absorber(litros)


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

from dataclasses import dataclass
from .arbol import Arbol

@dataclass
class Olivo(Arbol):
    tipo_aceituna: str = "Arbequina"

    def absorber(self, litros: float) -> None:
        super().absorber(litros)
        # regla: +0.01 m por riego
        if litros > 0:
            self.altura_m += 0.01


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

from dataclasses import dataclass
from .arbol import Arbol

@dataclass
class Pino(Arbol):
    variedad: str = "Parana"

    def absorber(self, litros: float) -> None:
        super().absorber(litros)
        # regla de crecimiento, +0.10 m por riego
        if litros > 0:
            self.altura_m += 0.10


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ================================================================================



# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

from dataclasses import dataclass
from .hortaliza import Hortaliza

@dataclass
class Zanahoria(Hortaliza):
    baby: bool = False

    def absorber(self, litros: float) -> None:
        super().absorber(litros)


