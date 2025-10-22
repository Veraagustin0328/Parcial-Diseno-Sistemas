from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import ABSORCION_L_ARBOL, ABSORCION_L_HORTALIZA
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Implementación constante: absorbe un máximo fijo según tipo."""

    def absorber(self, cultivo, litros: float) -> None:
        if isinstance(cultivo, Arbol):
            cultivo.absorber(min(litros, ABSORCION_L_ARBOL))
        elif isinstance(cultivo, Hortaliza):
            cultivo.absorber(min(litros, ABSORCION_L_HORTALIZA))
        else:
            cultivo.absorber(litros)
