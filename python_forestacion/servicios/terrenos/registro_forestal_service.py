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
