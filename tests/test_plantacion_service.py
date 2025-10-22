import pytest
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.excepciones import (
    SuperficieInsuficienteException,
    AguaAgotadaException,
)

def test_plantar_superficie_ok():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=20, agua_disponible_l=100)
    svc = PlantacionService()
    pino = Pino(nombre="P1", superficie_m2=10)

    svc.plantar(plant, pino)

    assert pino in plant.cultivos
    assert plant.superficie_disponible_m2 == 10

def test_plantar_superficie_insuficiente():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=5, agua_disponible_l=100)
    svc = PlantacionService()
    lechuga = Lechuga(nombre="L1", superficie_m2=6)

    with pytest.raises(SuperficieInsuficienteException):
        svc.plantar(plant, lechuga)

def test_regar_ok_y_actualiza_agua_y_cultivo():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=20, agua_disponible_l=10)
    svc = PlantacionService()
    pino = Pino(nombre="P1", superficie_m2=5)
    svc.plantar(plant, pino)

    svc.regar(plant, pino, litros=2.5)

    assert plant.agua_disponible_l == 7.5
    assert pino.agua_acumulada_l == 2.5

def test_regar_litros_invalidos():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=20, agua_disponible_l=10)
    svc = PlantacionService()
    pino = Pino(nombre="P", superficie_m2=5)
    svc.plantar(plant, pino)

    with pytest.raises(ValueError):
        svc.regar(plant, pino, litros=0)

def test_regar_agua_agotada():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=20, agua_disponible_l=1.0)
    svc = PlantacionService()
    pino = Pino(nombre="P", superficie_m2=5)
    svc.plantar(plant, pino)

    with pytest.raises(AguaAgotadaException):
        svc.regar(plant, pino, litros=2.0)

def test_cosechar_por_tipo_filtra_correcto():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=50, agua_disponible_l=100)
    svc = PlantacionService()
    p1 = Pino(nombre="P1", superficie_m2=10)
    p2 = Pino(nombre="P2", superficie_m2=10)
    l1 = Lechuga(nombre="L1", superficie_m2=3)
    for c in (p1, p2, l1):
        svc.plantar(plant, c)

    solo_pinos = svc.cosechar_por_tipo(plant, Pino)
    assert solo_pinos == [p1, p2]
