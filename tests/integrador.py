"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\tests
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: conftest.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\tests\conftest.py
# ================================================================================

# Error al leer este archivo: 'utf-8' codec can't decode byte 0xed in position 37: invalid continuation byte


# ================================================================================
# ARCHIVO 2/6: test_cultivo_factory.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\tests\test_cultivo_factory.py
# ================================================================================

﻿import pytest
from python_forestacion.patrones.factory.cultivo_factory import crear_cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga

def test_factory_crea_pino_y_lechuga():
    p = crear_cultivo("pino", nombre="P1", superficie_m2=5)
    l = crear_cultivo("lechuga", nombre="L1", superficie_m2=2)
    assert isinstance(p, Pino)
    assert isinstance(l, Lechuga)
    assert p.nombre == "P1" and l.nombre == "L1"

def test_factory_tipo_no_soportado():
    with pytest.raises(ValueError):
        crear_cultivo("cactus", nombre="C1", superficie_m2=1)


# ================================================================================
# ARCHIVO 3/6: test_cultivo_services.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\tests\test_cultivo_services.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: test_plantacion_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\tests\test_plantacion_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: test_riego_control.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\tests\test_riego_control.py
# ================================================================================

﻿from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

def test_control_riega_cuando_condiciones_ok():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=100, agua_disponible_l=10)
    p = Pino(nombre="P1", superficie_m2=5)
    l = Lechuga(nombre="L1", superficie_m2=2)
    plant.agregar_cultivo(p)
    plant.agregar_cultivo(l)

    ctrl = ControlRiegoTask(litros_por_cultivo=1.5)
    ctrl.update(EventoSensor(tipo="temp", valor=12.0))
    ctrl.update(EventoSensor(tipo="hum", valor=40.0))

    assert ctrl.condiciones_ok() is True
    rego = ctrl.evaluar_y_regar(plant)
    assert rego is True
    assert plant.agua_disponible_l == 7.0
    assert p.agua_acumulada_l == 1.5
    assert l.agua_acumulada_l == 1.5

def test_control_no_riega_fuera_de_rango():
    plant = Plantacion(nombre="Finca", superficie_disponible_m2=100, agua_disponible_l=10)
    p = Pino(nombre="P1", superficie_m2=5)
    plant.agregar_cultivo(p)
    ctrl = ControlRiegoTask(litros_por_cultivo=1.0)

    ctrl.update(EventoSensor(tipo="temp", valor=20.0))
    ctrl.update(EventoSensor(tipo="hum", valor=40.0))

    assert ctrl.condiciones_ok() is False
    rego = ctrl.evaluar_y_regar(plant)
    assert rego is False
    assert plant.agua_disponible_l == 10
    assert p.agua_acumulada_l == 0.0


# ================================================================================
# ARCHIVO 6/6: test_tierra_registro_service.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\tests\test_tierra_registro_service.py
# ================================================================================

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


