"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\arbol_service.py
# ================================================================================

﻿from dataclasses import dataclass
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.arbol import Arbol

@dataclass
class ArbolService(CultivoService):
    def post_riego(self, cultivo: Arbol, litros: float) -> None:
        if litros > 0:
            cultivo.altura_m += 0.01


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\cultivo_service.py
# ================================================================================

from dataclasses import dataclass
from typing import Protocol
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class CrecimientoPostRiego(Protocol):
    def post_riego(self, cultivo: Cultivo, litros: float) -> None: ...

@dataclass
class CultivoService:
    """Template Method para regar un cultivo con Strategy de absorción."""
    absorcion: AbsorcionAguaStrategy = AbsorcionConstanteStrategy()

    def regar(self, cultivo: Cultivo, litros: float) -> None:
        if litros <= 0:
            return
        # Paso 1: absorber según Strategy
        self.absorcion.absorber(cultivo, litros)
        # Paso 2: gancho de crecimiento (override en subclases)
        self.post_riego(cultivo, litros)

    # hook
    def post_riego(self, cultivo: Cultivo, litros: float) -> None:
        """Por defecto no hace nada (subclases pueden crecer, cambiar estado, etc.)."""
        pass


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ================================================================================

﻿from __future__ import annotations
from typing import Dict, Type

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService


class CultivoServiceRegistry:
    _instance: "CultivoServiceRegistry | None" = None

    def __init__(self) -> None:
        self._map: Dict[Type[Cultivo], CultivoService] = {}
        self.register(Pino, PinoService())
        self.register(Lechuga, LechugaService())

    @classmethod
    def instance(cls) -> "CultivoServiceRegistry":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def register(self, tipo: Type[Cultivo], service: CultivoService) -> None:
        self._map[tipo] = service

    def resolve(self, cultivo: Cultivo) -> CultivoService:
        for tipo, svc in self._map.items():
            if isinstance(cultivo, tipo):
                return svc
        return CultivoService()


# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\lechuga_service.py
# ================================================================================

from dataclasses import dataclass
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.lechuga import Lechuga

@dataclass
class LechugaService(CultivoService):
    def post_riego(self, cultivo: Lechuga, litros: float) -> None:
        # Si recibe riego por primera vez, pasa de "semilla" a "creciendo"
        if litros > 0 and cultivo.estado == "semilla":
            cultivo.estado = "creciendo"


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\olivo_service.py
# ================================================================================



# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\pino_service.py
# ================================================================================

﻿from dataclasses import dataclass
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.entidades.cultivos.pino import Pino

@dataclass
class PinoService(ArbolService):
    def post_riego(self, cultivo: Pino, litros: float) -> None:
        if litros > 0:
            cultivo.altura_m += 0.10


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\cultivos\zanahoria_service.py
# ================================================================================



