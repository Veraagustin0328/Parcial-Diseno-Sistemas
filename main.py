from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.patrones.factory.cultivo_factory import crear_cultivo
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

SEP = "=" * 70
SUB = "-" * 70

def ok(msg: str):
    print(f"[OK] {msg}")

def main():
    print(SEP)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print(SEP)
    print()

    
    # PATRON SINGLETON
    
    print(SUB)
    print("  PATRON SINGLETON: Inicializando servicios")
    print(SUB)
    reg1 = CultivoServiceRegistry.instance()
    reg2 = CultivoServiceRegistry.instance()
    assert reg1 is reg2
    ok("Todos los servicios comparten la misma instancia del Registry")
    print()

  
    # FACTORY + ENTIDADES
    
    print("1. Creando tierra con plantacion...")
    plantacion = Plantacion(nombre="Finca Demo", superficie_disponible_m2=100, agua_disponible_l=15)

    print("2. Creando cultivos con Factory Method...")
    pino = crear_cultivo("pino", nombre="Pino1", superficie_m2=5)
    lechuga = crear_cultivo("lechuga", nombre="Lechuga1", superficie_m2=2)
    plantacion.agregar_cultivo(pino)
    plantacion.agregar_cultivo(lechuga)
    ok("Factory: cultivos creados e incorporados a la plantacion")
    print(f"   -> Agua disponible: {plantacion.agua_disponible_l} L")
    print()

   
    # OBSERVER + STRATEGY
   
    print("3. Iniciando sistema de riego (Observer + Strategy)")
    temp_sensor = TemperaturaReaderTask()
    hum_sensor = HumedadReaderTask()
    ctrl = ControlRiegoTask(litros_por_cultivo=2.0)

    # Observer: el controlador se suscribe a los sensores
    temp_sensor.attach(ctrl)
    hum_sensor.attach(ctrl)

    # Emitimos eventos de sensores (notifican al controlador)
    temp_sensor.emular(12.0)  # dentro de 8..15
    hum_sensor.emular(40.0)   # < 50

    if ctrl.condiciones_ok():
        rego = ctrl.evaluar_y_regar(plantacion)
        if rego:
            ok("Observer: eventos recibidos correctamente")
            ok("Strategy: absorcion aplicada segun tipo de cultivo")
        else:
            print("No se pudo regar (agua insuficiente).")
    else:
        print("Condiciones de riego NO adecuadas; no se riega.")
    print()

    print("4. Estado final:")
    print(f"   -> Agua restante: {plantacion.agua_disponible_l} L")
    print(f"   -> {pino.nombre}: {pino.agua_acumulada_l} L, altura: {getattr(pino, 'altura_m', 0):.2f} m")
    print(f"   -> {lechuga.nombre}: {lechuga.agua_acumulada_l} L, estado: {getattr(lechuga, 'estado', 'n/a')}")
    print()

  
    # RESUMEN FINAL 
    
    print(SEP)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print(SEP)
    ok("SINGLETON   - CultivoServiceRegistry (instancia unica)")
    ok("FACTORY     - Creacion de cultivos")
    ok("OBSERVER    - Sistema de sensores y eventos")
    ok("STRATEGY    - Algoritmos de absorcion de agua")
    print(SEP)

if __name__ == "__main__":
    main()
