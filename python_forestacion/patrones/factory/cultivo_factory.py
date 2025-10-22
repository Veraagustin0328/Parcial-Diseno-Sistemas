from typing import Type
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
_MAP: dict[str, Type[Cultivo]] = {"pino": Pino,"lechuga": Lechuga,"olivo": Olivo,"zanahoria": Zanahoria}
def crear_cultivo(tipo: str, **kwargs) -> Cultivo:
    cls = _MAP.get(tipo.lower())
    if cls is None:
        raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
    return cls(**kwargs)
