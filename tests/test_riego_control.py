from python_forestacion.entidades.terrenos.plantacion import Plantacion
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
