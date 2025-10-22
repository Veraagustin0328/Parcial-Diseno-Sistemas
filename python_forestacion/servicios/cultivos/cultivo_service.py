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
