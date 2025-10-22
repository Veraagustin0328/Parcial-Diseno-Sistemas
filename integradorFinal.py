"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:/Users/veraa\ParcialMendoza\PythonForestal\.
Fecha de generacion: 2025-10-21 23:28:07
Total de archivos integrados: 74
Total de directorios procesados: 23
============================================================================
"""

from __future__ import annotations
from __future__ import annotations




# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. buscar_paquete.py
#   2. main.py
#
# DIRECTORIO: python_forestacion
#   3. __init__.py
#   4. constantes.py
#
# DIRECTORIO: python_forestacion\entidades
#   5. __init__.py
#
# DIRECTORIO: python_forestacion/entidades/cultivos
#   6. __init__.py
#   7. arbol.py
#   8. cultivo.py
#   9. hortaliza.py
#   10. lechuga.py
#   11. olivo.py
#   12. pino.py
#   13. tipo_aceituna.py
#   14. zanahoria.py
#
# DIRECTORIO: python_forestacion/entidades/personal
#   15. __init__.py
#   16. apto_medico.py
#   17. herramienta.py
#   18. tarea.py
#   19. trabajador.py
#
# DIRECTORIO: python_forestacion/entidades/terrenos
#   20. __init__.py
#   21. plantacion.py
#   22. registro_forestal.py
#   23. tierra.py
#
# DIRECTORIO: python_forestacion\excepciones
#   24. __init__.py
#   25. agua_agotada_exception.py
#   26. forestacion_exception.py
#   27. mensajes_exception.py
#   28. persistencia_exception.py
#   29. superficie_insuficiente_exception.py
#
# DIRECTORIO: python_forestacion\patrones
#   30. __init__.py
#
# DIRECTORIO: python_forestacion/patrones/factory
#   31. __init__.py
#   32. cultivo_factory.py
#
# DIRECTORIO: python_forestacion/patrones/observer
#   33. __init__.py
#   34. observable.py
#   35. observer.py
#
# DIRECTORIO: python_forestacion/patrones/observer\eventos
#   36. __init__.py
#   37. evento_plantacion.py
#   38. evento_sensor.py
#
# DIRECTORIO: python_forestacion/patrones/singleton
#   39. __init__.py
#
# DIRECTORIO: python_forestacion/patrones/strategy
#   40. __init__.py
#   41. absorcion_agua_strategy.py
#
# DIRECTORIO: python_forestacion/patrones/strategy\impl
#   42. __init__.py
#   43. absorcion_constante_strategy.py
#   44. absorcion_seasonal_strategy.py
#
# DIRECTORIO: python_forestacion\riego
#   45. __init__.py
#
# DIRECTORIO: python_forestacion/riego/control
#   46. __init__.py
#   47. control_riego_task.py
#
# DIRECTORIO: python_forestacion/riego/sensores
#   48. __init__.py
#   49. humedad_reader_task.py
#   50. temperatura_reader_task.py
#
# DIRECTORIO: python_forestacion\servicios
#   51. __init__.py
#
# DIRECTORIO: python_forestacion/servicios/cultivos
#   52. __init__.py
#   53. arbol_service.py
#   54. cultivo_service.py
#   55. cultivo_service_registry.py
#   56. lechuga_service.py
#   57. olivo_service.py
#   58. pino_service.py
#   59. zanahoria_service.py
#
# DIRECTORIO: python_forestacion/servicios/negocio
#   60. __init__.py
#   61. fincas_service.py
#   62. paquete.py
#
# DIRECTORIO: python_forestacion/servicios/personal
#   63. __init__.py
#   64. trabajador_service.py
#
# DIRECTORIO: python_forestacion/servicios/terrenos
#   65. __init__.py
#   66. plantacion_service.py
#   67. registro_forestal_service.py
#   68. tierra_service.py
#
# DIRECTORIO: tests
#   69. conftest.py
#   70. test_cultivo_factory.py
#   71. test_cultivo_services.py
#   72. test_plantacion_service.py
#   73. test_riego_control.py
#   74. test_tierra_registro_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/74: buscar_paquete.py
# Directorio: .
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\.\buscar_paquete.py
# ==============================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


#if __name__ == "__main__":
#   sys.exit(main())

# ==============================================================================
# ARCHIVO 2/74: main.py
# Directorio: .
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\.\main.py
# ==============================================================================

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
    import sys; sys.exit(0)



################################################################################
# DIRECTORIO: python_forestacion
################################################################################

# ==============================================================================
# ARCHIVO 3/74: __init__.py
# Directorio: python_forestacion
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/74: constantes.py
# Directorio: python_forestacion
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/constantes.py
# ==============================================================================

TEMP_MIN_RIEGO = 8.0
TEMP_MAX_RIEGO = 15.0
HUM_MAX_RIEGO  = 50.0

ABSORCION_L_HORTALIZA = 1.0
ABSORCION_L_ARBOL     = 2.0



################################################################################
# DIRECTORIO: python_forestacion\entidades
################################################################################

# ==============================================================================
# ARCHIVO 5/74: __init__.py
# Directorio: python_forestacion\entidades
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 6/74: __init__.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 7/74: arbol.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

from dataclasses import dataclass
from .cultivo import Cultivo

@dataclass
class Arbol(Cultivo):
    altura_m: float = 0.0  # árboles crecen por riego

    def absorber(self, litros: float) -> None:
        if litros <= 0:
            return
        self.agua_acumulada_l += litros


# ==============================================================================
# ARCHIVO 8/74: cultivo.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Cultivo(ABC):
    nombre: str
    superficie_m2: float
    agua_acumulada_l: float = 0.0

    @abstractmethod
    def absorber(self, litros: float) -> None:
        """Cada cultivo define cómo “consume/absorbe” agua al regar."""
        raise NotImplementedError


# ==============================================================================
# ARCHIVO 9/74: hortaliza.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

from dataclasses import dataclass
from cultivo import Cultivo

@dataclass
class Hortaliza(Cultivo):
    estado: str = "semilla"  # estado simple para ejemplo

    def absorber(self, litros: float) -> None:
        if litros <= 0:
            return
        self.agua_acumulada_l += litros


# ==============================================================================
# ARCHIVO 10/74: lechuga.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

from dataclasses import dataclass
from hortaliza import Hortaliza

@dataclass
class Lechuga(Hortaliza):
    variedad: str = "Crespa"

    def absorber(self, litros: float) -> None:
        # hortalizas: absorción constante (1–2L típicamente, lo maneja el servicio)
        super().absorber(litros)


# ==============================================================================
# ARCHIVO 11/74: olivo.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

from dataclasses import dataclass
from arbol import Arbol

@dataclass
class Olivo(Arbol):
    tipo_aceituna: str = "Arbequina"

    def absorber(self, litros: float) -> None:
        super().absorber(litros)
        # regla: +0.01 m por riego
        if litros > 0:
            self.altura_m += 0.01


# ==============================================================================
# ARCHIVO 12/74: pino.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

from dataclasses import dataclass
from arbol import Arbol

@dataclass
class Pino(Arbol):
    variedad: str = "Parana"

    def absorber(self, litros: float) -> None:
        super().absorber(litros)
        # regla de crecimiento, +0.10 m por riego
        if litros > 0:
            self.altura_m += 0.10


# ==============================================================================
# ARCHIVO 13/74: tipo_aceituna.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 14/74: zanahoria.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

from dataclasses import dataclass
from hortaliza import Hortaliza

@dataclass
class Zanahoria(Hortaliza):
    baby: bool = False

    def absorber(self, litros: float) -> None:
        super().absorber(litros)



################################################################################
# DIRECTORIO: python_forestacion/entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 15/74: __init__.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 16/74: apto_medico.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 17/74: herramienta.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/personal/herramienta.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 18/74: tarea.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/personal/tarea.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/74: trabajador.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/personal/trabajador.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 20/74: __init__.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 21/74: plantacion.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

from dataclasses import dataclass, field
from typing import List
from cultivos.cultivo import Cultivo

@dataclass
class Plantacion:
    nombre: str
    superficie_disponible_m2: float
    agua_disponible_l: float
    cultivos: List[Cultivo] = field(default_factory=list)

    def agregar_cultivo(self, cultivo: Cultivo) -> None:
        self.cultivos.append(cultivo)
        self.superficie_disponible_m2 -= cultivo.superficie_m2


# ==============================================================================
# ARCHIVO 22/74: registro_forestal.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

from dataclasses import dataclass, field
from typing import List
from python_forestacion.entidades.terrenos.tierra import Tierra

@dataclass
class RegistroForestal:
    nombre: str
    tierras: List[Tierra] = field(default_factory=list)

    def alta_tierra(self, tierra: Tierra) -> None:
        """Agrega una tierra al registro."""
        self.tierras.append(tierra)


# ==============================================================================
# ARCHIVO 23/74: tierra.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

from dataclasses import dataclass
from typing import Optional
from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class Tierra:
    padron: int
    superficie_total_m2: float
    domicilio: str
    plantacion: Optional[Plantacion] = None



################################################################################
# DIRECTORIO: python_forestacion\excepciones
################################################################################

# ==============================================================================
# ARCHIVO 24/74: __init__.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/excepciones\__init__.py
# ==============================================================================

from forestacion_exception import ForestacionException
from superficie_insuficiente_exception import SuperficieInsuficienteException
from agua_agotada_exception import AguaAgotadaException
from persistencia_exception import PersistenciaException

__all__ = [
    "ForestacionException",
    "SuperficieInsuficienteException",
    "AguaAgotadaException",
    "PersistenciaException",
]


# ==============================================================================
# ARCHIVO 25/74: agua_agotada_exception.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/excepciones\agua_agotada_exception.py
# ==============================================================================

from forestacion_exception import ForestacionException
class AguaAgotadaException(ForestacionException):
    """No hay agua suficiente para realizar la operacion."""
    pass


# ==============================================================================
# ARCHIVO 26/74: forestacion_exception.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/excepciones\forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """Excepcion base del dominio Forestacion."""
    pass


# ==============================================================================
# ARCHIVO 27/74: mensajes_exception.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/excepciones\mensajes_exception.py
# ==============================================================================

MSJ_SUPERFICIE_INSUFICIENTE = "Superficie insuficiente para plantar."
MSJ_AGUA_AGOTADA           = "No hay agua suficiente en la plantacion."
MSJ_LITROS_INVALIDOS       = "Los litros de riego deben ser > 0."


# ==============================================================================
# ARCHIVO 28/74: persistencia_exception.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/excepciones\persistencia_exception.py
# ==============================================================================

from forestacion_exception import ForestacionException
class PersistenciaException(ForestacionException):
    """Error de lectura/escritura en persistencia."""
    pass


# ==============================================================================
# ARCHIVO 29/74: superficie_insuficiente_exception.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/excepciones\superficie_insuficiente_exception.py
# ==============================================================================

from forestacion_exception import ForestacionException
class SuperficieInsuficienteException(ForestacionException):
    """Se intenta plantar superando la superficie disponible."""
    pass



################################################################################
# DIRECTORIO: python_forestacion\patrones
################################################################################

# ==============================================================================
# ARCHIVO 30/74: __init__.py
# Directorio: python_forestacion\patrones
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 31/74: __init__.py
# Directorio: python_forestacion/patrones/factory
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/74: cultivo_factory.py
# Directorio: python_forestacion/patrones/factory
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: python_forestacion/patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 33/74: __init__.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 34/74: observable.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/observer/observable.py
# ==============================================================================

from typing import Generic, List, TypeVar
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

class Observable(Generic[T]):
    def __init__(self) -> None:
        self._observers: List[Observer[T]] = []

    def attach(self, observer: Observer[T]) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer[T]) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event: T) -> None:
        for obs in self._observers:
            obs.update(event)


# ==============================================================================
# ARCHIVO 35/74: observer.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/observer/observer.py
# ==============================================================================

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

class Observer(ABC, Generic[T]):
    @abstractmethod
    def update(self, event: T) -> None:
        pass



################################################################################
# DIRECTORIO: python_forestacion/patrones/observer\eventos
################################################################################

# ==============================================================================
# ARCHIVO 36/74: __init__.py
# Directorio: python_forestacion/patrones/observer\eventos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/observer/eventos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/74: evento_plantacion.py
# Directorio: python_forestacion/patrones/observer\eventos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/observer/eventos\evento_plantacion.py
# ==============================================================================

from dataclasses import dataclass

@dataclass
class EventoPlantacion:
    mensaje: str


# ==============================================================================
# ARCHIVO 38/74: evento_sensor.py
# Directorio: python_forestacion/patrones/observer\eventos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/observer/eventos\evento_sensor.py
# ==============================================================================

from dataclasses import dataclass

@dataclass
class EventoSensor:
    tipo: str
    valor: float



################################################################################
# DIRECTORIO: python_forestacion/patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 39/74: __init__.py
# Directorio: python_forestacion/patrones/singleton
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/singleton/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 40/74: __init__.py
# Directorio: python_forestacion/patrones/strategy
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/74: absorcion_agua_strategy.py
# Directorio: python_forestacion/patrones/strategy
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz Strategy: define como un cultivo absorbe agua."""
    @abstractmethod
    def absorber(self, cultivo: Cultivo, litros: float) -> None:
        pass



################################################################################
# DIRECTORIO: python_forestacion/patrones/strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 42/74: __init__.py
# Directorio: python_forestacion/patrones/strategy\impl
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/strategy/impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 43/74: absorcion_constante_strategy.py
# Directorio: python_forestacion/patrones/strategy\impl
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/strategy/impl\absorcion_constante_strategy.py
# ==============================================================================

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import ABSORCION_L_ARBOL, ABSORCION_L_HORTALIZA
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Implementacion constante: absorbe un maximo fijo segun tipo."""
    def absorber(self, cultivo, litros: float) -> None:
        if isinstance(cultivo, Arbol):
            cultivo.absorber(min(litros, ABSORCION_L_ARBOL))
        elif isinstance(cultivo, Hortaliza):
            cultivo.absorber(min(litros, ABSORCION_L_HORTALIZA))
        else:
            cultivo.absorber(litros)


# ==============================================================================
# ARCHIVO 44/74: absorcion_seasonal_strategy.py
# Directorio: python_forestacion/patrones/strategy\impl
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/patrones/strategy/impl\absorcion_seasonal_strategy.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion\riego
################################################################################

# ==============================================================================
# ARCHIVO 45/74: __init__.py
# Directorio: python_forestacion\riego
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/riego/control
################################################################################

# ==============================================================================
# ARCHIVO 46/74: __init__.py
# Directorio: python_forestacion/riego/control
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/74: control_riego_task.py
# Directorio: python_forestacion/riego/control
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

from dataclasses import dataclass, field
from typing import Optional
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUM_MAX_RIEGO
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

@dataclass
class ControlRiegoTask:
    litros_por_cultivo: float = 1.0
    _ultima_temp: Optional[float] = field(default=None, init=False, repr=False)
    _ultima_hum: Optional[float] = field(default=None, init=False, repr=False)

    def update(self, event: EventoSensor) -> None:
        if event.tipo == "temp":
            self._ultima_temp = event.valor
        elif event.tipo == "hum":
            self._ultima_hum = event.valor

    def condiciones_ok(self) -> bool:
        if self._ultima_temp is None or self._ultima_hum is None:
            return False
        return (TEMP_MIN_RIEGO <= self._ultima_temp <= TEMP_MAX_RIEGO) and (self._ultima_hum < HUM_MAX_RIEGO)

    def evaluar_y_regar(self, plantacion: Plantacion) -> bool:
        if not self.condiciones_ok():
            return False
        svc = PlantacionService()
        rego = False
        for c in list(plantacion.cultivos):
            if plantacion.agua_disponible_l >= self.litros_por_cultivo:
                svc.regar(plantacion, c, self.litros_por_cultivo)
                rego = True
            else:
                break
        return rego



################################################################################
# DIRECTORIO: python_forestacion/riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 48/74: __init__.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 49/74: humedad_reader_task.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

from dataclasses import dataclass
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

@dataclass
class HumedadReaderTask(Observable[EventoSensor]):
    def __init__(self) -> None:
        super().__init__()
    def emular(self, hum: float) -> None:
        self.notify(EventoSensor(tipo="hum", valor=hum))


# ==============================================================================
# ARCHIVO 50/74: temperatura_reader_task.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

from dataclasses import dataclass
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

@dataclass
class TemperaturaReaderTask(Observable[EventoSensor]):
    def __init__(self) -> None:
        super().__init__()
    def emular(self, temp: float) -> None:
        self.notify(EventoSensor(tipo="temp", valor=temp))



################################################################################
# DIRECTORIO: python_forestacion\servicios
################################################################################

# ==============================================================================
# ARCHIVO 51/74: __init__.py
# Directorio: python_forestacion\servicios
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 52/74: __init__.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 53/74: arbol_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

from dataclasses import dataclass
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.arbol import Arbol

@dataclass
class ArbolService(CultivoService):
    def post_riego(self, cultivo: Arbol, litros: float) -> None:
        if litros > 0:
            cultivo.altura_m += 0.01


# ==============================================================================
# ARCHIVO 54/74: cultivo_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

from dataclasses import dataclass
from typing import Protocol
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class CrecimientoPostRiego(Protocol):
    def post_riego(self, cultivo: Cultivo, litros: float) -> None: ...

@dataclass
class CultivoService:
    """Template Method para regar un cultivo con Strategy de absorción."""
    absorcion: AbsorcionAguaStrategy = AbsorcionConstanteStrategy()

    def regar(self, cultivo: Cultivo, litros: float) -> None:
        if litros <= 0:
            return
        # Paso 1: absorber según Strategy
        self.absorcion.absorber(cultivo, litros)
        # Paso 2: gancho de crecimiento (override en subclases)
        self.post_riego(cultivo, litros)

    # hook
    def post_riego(self, cultivo: Cultivo, litros: float) -> None:
        """Por defecto no hace nada (subclases pueden crecer, cambiar estado, etc.)."""
        pass


# ==============================================================================
# ARCHIVO 55/74: cultivo_service_registry.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

from typing import Dict, Type

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService


class CultivoServiceRegistry:
    _instance: "CultivoServiceRegistry | None" = None

    def __init__(self) -> None:
        self._map: Dict[Type[Cultivo], CultivoService] = {}
        self.register(Pino, PinoService())
        self.register(Lechuga, LechugaService())

    @classmethod
    def instance(cls) -> "CultivoServiceRegistry":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def register(self, tipo: Type[Cultivo], service: CultivoService) -> None:
        self._map[tipo] = service

    def resolve(self, cultivo: Cultivo) -> CultivoService:
        for tipo, svc in self._map.items():
            if isinstance(cultivo, tipo):
                return svc
        return CultivoService()


# ==============================================================================
# ARCHIVO 56/74: lechuga_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from dataclasses import dataclass
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.lechuga import Lechuga

@dataclass
class LechugaService(CultivoService):
    def post_riego(self, cultivo: Lechuga, litros: float) -> None:
        # Si recibe riego por primera vez, pasa de "semilla" a "creciendo"
        if litros > 0 and cultivo.estado == "semilla":
            cultivo.estado = "creciendo"


# ==============================================================================
# ARCHIVO 57/74: olivo_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 58/74: pino_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

from dataclasses import dataclass
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.entidades.cultivos.pino import Pino

@dataclass
class PinoService(ArbolService):
    def post_riego(self, cultivo: Pino, litros: float) -> None:
        if litros > 0:
            cultivo.altura_m += 0.10


# ==============================================================================
# ARCHIVO 59/74: zanahoria_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 60/74: __init__.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 61/74: fincas_service.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 62/74: paquete.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/negocio/paquete.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 63/74: __init__.py
# Directorio: python_forestacion/servicios/personal
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 64/74: trabajador_service.py
# Directorio: python_forestacion/servicios/personal
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 65/74: __init__.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 66/74: plantacion_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from dataclasses import dataclass
from typing import Type, List, TypeVar

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.excepciones import (
    SuperficieInsuficienteException,
    AguaAgotadaException,
)
from python_forestacion.excepciones.mensajes_exception import (
    MSJ_SUPERFICIE_INSUFICIENTE,
    MSJ_AGUA_AGOTADA,
    MSJ_LITROS_INVALIDOS,
)

T = TypeVar("T", bound=Cultivo)

@dataclass
class PlantacionService:
    def plantar(self, plantacion: Plantacion, cultivo: Cultivo) -> None:
        if cultivo.superficie_m2 > plantacion.superficie_disponible_m2:
            raise SuperficieInsuficienteException(MSJ_SUPERFICIE_INSUFICIENTE)
        plantacion.agregar_cultivo(cultivo)

    def regar(self, plantacion: Plantacion, cultivo: Cultivo, litros: float) -> None:
        if litros <= 0:
            raise ValueError(MSJ_LITROS_INVALIDOS)
        if plantacion.agua_disponible_l < litros:
            raise AguaAgotadaException(MSJ_AGUA_AGOTADA)
        plantacion.agua_disponible_l -= litros
        cultivo.absorber(litros)

    def cosechar_por_tipo(self, plantacion: Plantacion, tipo: Type[T]) -> List[T]:
        return [c for c in plantacion.cultivos if isinstance(c, tipo)]


# ==============================================================================
# ARCHIVO 67/74: registro_forestal_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 68/74: tierra_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

from dataclasses import dataclass
from typing import Optional
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class TierraService:
    def asignar_plantacion(self, tierra: Tierra, plantacion: Plantacion) -> None:
        """Asigna una plantacion a la tierra (reemplaza si ya hubiera)."""
        tierra.plantacion = plantacion

    def get_plantacion(self, tierra: Tierra) -> Optional[Plantacion]:
        """Devuelve la plantacion o None si no hay."""
        return tierra.plantacion



################################################################################
# DIRECTORIO: tests
################################################################################

# ==============================================================================
# ARCHIVO 69/74: conftest.py
# Directorio: tests
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./tests/conftest.py
# ==============================================================================

# Error al leer este archivo: 'utf-8' codec can't decode byte 0xed in position 37: invalid continuation byte


# ==============================================================================
# ARCHIVO 70/74: test_cultivo_factory.py
# Directorio: tests
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./tests/test_cultivo_factory.py
# ==============================================================================

import pytest
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


# ==============================================================================
# ARCHIVO 71/74: test_cultivo_services.py
# Directorio: tests
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./tests/test_cultivo_services.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 72/74: test_plantacion_service.py
# Directorio: tests
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./tests/test_plantacion_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 73/74: test_riego_control.py
# Directorio: tests
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./tests/test_riego_control.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 74/74: test_tierra_registro_service.py
# Directorio: tests
# Ruta completa: C:/Users/veraa\ParcialMendoza\PythonForestal\./tests/test_tierra_registro_service.py
# ==============================================================================

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



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 74
# Generado: 2025-10-21 23:28:07
################################################################################


if __name__ == "__main__":
    main()
    import sys; sys.exit(0)
    import sys
    sys.exit(0)

