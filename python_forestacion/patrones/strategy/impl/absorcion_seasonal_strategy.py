from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Absorción que varía según estación (invierno/verano)."""

    def absorber(self, cultivo, litros: float) -> None:
        month = date.today().month
        factor = 1.0 if month in (12, 1, 2) else (0.5 if month in (6, 7, 8) else 0.75)
        cultivo.absorber(litros * factor)
