from __future__ import annotations
from typing import Dict, Type, Any
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

class CultivoServiceRegistry:
    _instance: "CultivoServiceRegistry" | None = None

    def __init__(self) -> None:
        self._map: Dict[Type[Cultivo], CultivoService] = {}
        # registro por defecto
        self.register(Pino, PinoService())
        self.register(Lechuga, LechugaService())

    @classmethod
    def instance(cls) -> "CultivoServiceRegistry":
        if cls._instance is None:
            cls._instance = CultivoServiceRegistry()
        return cls._instance

    def register(self, tipo: Type[Cultivo], service: CultivoService) -> None:
        self._map[tipo] = service

    def resolve(self, cultivo: Cultivo) -> CultivoService:
        # busca por tipo exacto o por superclase
        for key, svc in self._map.items():
            if isinstance(cultivo, key):
                return svc
        # fallback genérico
        return CultivoService()
