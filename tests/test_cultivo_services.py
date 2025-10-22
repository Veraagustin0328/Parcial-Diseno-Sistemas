from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService

def test_registry_resuelve_servicio_correcto():
    reg = CultivoServiceRegistry.instance()
    assert isinstance(reg.resolve(Pino(nombre="P1", superficie_m2=5)), PinoService)
    assert isinstance(reg.resolve(Lechuga(nombre="L1", superficie_m2=2)), LechugaService)

def test_pino_crece_mas_al_regar():
    p = Pino(nombre="P", superficie_m2=5)
    svc = PinoService()
    svc.regar(p, 2.0)
    assert p.agua_acumulada_l > 0
    assert p.altura_m >= 0.10  # crecimiento del pino

def test_lechuga_cambia_estado_con_riego():
    l = Lechuga(nombre="L", superficie_m2=1)
    svc = LechugaService()
    assert l.estado == "semilla"
    svc.regar(l, 1.0)
    assert l.estado == "creciendo"
