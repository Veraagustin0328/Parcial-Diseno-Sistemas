"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\terrenos
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\terrenos\plantacion_service.py
# ================================================================================

from dataclasses import dataclass
from typing import Type, List, TypeVar

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.excepciones import (
    SuperficieInsuficienteException,
    AguaAgotadaException,
)
from python_forestacion.excepciones.mensajes_exception import (
    MSJ_SUPERFICIE_INSUFICIENTE,
    MSJ_AGUA_AGOTADA,
    MSJ_LITROS_INVALIDOS,
)

T = TypeVar("T", bound=Cultivo)

@dataclass
class PlantacionService:
    def plantar(self, plantacion: Plantacion, cultivo: Cultivo) -> None:
        if cultivo.superficie_m2 > plantacion.superficie_disponible_m2:
            raise SuperficieInsuficienteException(MSJ_SUPERFICIE_INSUFICIENTE)
        plantacion.agregar_cultivo(cultivo)

    def regar(self, plantacion: Plantacion, cultivo: Cultivo, litros: float) -> None:
        if litros <= 0:
            raise ValueError(MSJ_LITROS_INVALIDOS)
        if plantacion.agua_disponible_l < litros:
            raise AguaAgotadaException(MSJ_AGUA_AGOTADA)
        plantacion.agua_disponible_l -= litros
        cultivo.absorber(litros)

    def cosechar_por_tipo(self, plantacion: Plantacion, tipo: Type[T]) -> List[T]:
        return [c for c in plantacion.cultivos if isinstance(c, tipo)]


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ================================================================================

from dataclasses import dataclass
from typing import List, Optional
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.terrenos.tierra import Tierra

@dataclass
class RegistroForestalService:
    def alta_tierra(self, registro: RegistroForestal, tierra: Tierra) -> None:
        registro.alta_tierra(tierra)

    def listar_tierras(self, registro: RegistroForestal) -> List[Tierra]:
        return list(registro.tierras)

    def buscar_por_padron(self, registro: RegistroForestal, padron: int) -> Optional[Tierra]:
        for t in registro.tierras:
            if t.padron == padron:
                return t
        return None


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\servicios\terrenos\tierra_service.py
# ================================================================================

from dataclasses import dataclass
from typing import Optional
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class TierraService:
    def asignar_plantacion(self, tierra: Tierra, plantacion: Plantacion) -> None:
        """Asigna una plantacion a la tierra (reemplaza si ya hubiera)."""
        tierra.plantacion = plantacion

    def get_plantacion(self, tierra: Tierra) -> Optional[Plantacion]:
        """Devuelve la plantacion o None si no hay."""
        return tierra.plantacion


