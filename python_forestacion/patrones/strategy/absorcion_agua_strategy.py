from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz Strategy: define cómo un cultivo absorbe agua."""

    @abstractmethod
    def absorber(self, cultivo: Cultivo, litros: float) -> None:
        """Aplica la lógica de absorción de agua al cultivo."""
        pass
        