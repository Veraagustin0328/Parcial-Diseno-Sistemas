from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

def test_asignar_y_leer_plantacion_en_tierra():
    tierra = Tierra(padron=100, superficie_total_m2=1000, domicilio="Ruta X")
    plant = Plantacion(nombre="Finca A", superficie_disponible_m2=800, agua_disponible_l=200)
    svc = TierraService()

    # al inicio no hay plantacion
    assert svc.get_plantacion(tierra) is None

    # asignar
    svc.asignar_plantacion(tierra, plant)
    assert svc.get_plantacion(tierra) is plant

def test_registro_alta_listar_buscar():
    reg = RegistroForestal(nombre="Registro Mendoza")
    rsvc = RegistroForestalService()

    t1 = Tierra(padron=1, superficie_total_m2=500, domicilio="Km 1")
    t2 = Tierra(padron=2, superficie_total_m2=750, domicilio="Km 2")

    rsvc.alta_tierra(reg, t1)
    rsvc.alta_tierra(reg, t2)

    tierras = rsvc.listar_tierras(reg)
    assert tierras == [t1, t2]

    encontrado = rsvc.buscar_por_padron(reg, 2)
    assert encontrado is t2

    no_existe = rsvc.buscar_por_padron(reg, 999)
    assert no_existe is None
