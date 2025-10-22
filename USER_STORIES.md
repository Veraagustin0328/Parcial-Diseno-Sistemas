Historias de Usuario — Sistema Forestal Integrador
Contexto General

El proyecto PythonForestal modela una finca agrícola donde se administran tierras, plantaciones y distintos tipos de cultivos.
El sistema automatiza parte del proceso de riego mediante sensores virtuales y aplica cuatro patrones de diseño fundamentales: Singleton, Factory Method, Observer y Strategy.

Se desarrolla en Python con arquitectura modular y pruebas unitarias que garantizan el correcto funcionamiento de cada servicio.

Épica 1 — Administración de Tierras y Plantaciones
HU-1.1 — Registrar una nueva Tierra

Como operador del sistema
Quiero registrar una nueva tierra en el sistema forestal
Para asociarla luego a futuras plantaciones

Criterios de aceptación

Given un registro forestal vacío

When se crea una tierra con número de padrón, superficie y ubicación

Then la tierra se almacena correctamente y aparece disponible para uso.

Referencia

entidades/terrenos/tierra.py

servicios/terrenos/tierra_service.py

Test: tests/test_tierra_registro_service.py

HU-1.2 — Crear una Plantación en una Tierra

Como administrador
Quiero crear una plantación asociada a una tierra existente
Para organizar los cultivos dentro del terreno

Criterios de aceptación

Given una tierra registrada

When se crea una Plantacion con superficie y agua disponible

Then se asocia correctamente a la tierra y puede contener cultivos.

Referencia

entidades/terrenos/plantacion.py

servicios/terrenos/plantacion_service.py

Épica 2 — Gestión de Cultivos
HU-2.1 — Crear cultivos a partir de su tipo

Como capataz
Quiero generar distintos tipos de cultivos según su clase (Pino, Lechuga, etc.)
Para automatizar su creación y manejo

Criterios de aceptación

Given el tipo solicitado

When se llama al método Factory con "pino" o "lechuga"

Then se instancia el cultivo correspondiente.

Si el tipo no existe, se lanza una excepción.

Referencia

patrones/factory/cultivo_factory.py

Test: tests/test_cultivo_factory.py

HU-2.2 — Agregar un cultivo a la plantación

Como responsable del campo
Quiero agregar cultivos a una plantación existente
Para tener un control del espacio utilizado y los litros de agua consumidos

Criterios de aceptación

Given una plantación con espacio disponible

When se agrega un cultivo

Then se descuenta la superficie y se actualiza el registro de cultivos.

Si no hay espacio, lanza SuperficieInsuficienteException.

Referencia

servicios/terrenos/plantacion_service.py

excepciones/superficie_insuficiente_exception.py

Test: tests/test_plantacion_service.py

Épica 3 — Sistema de Riego (Observer + Strategy)
HU-3.1 — Detectar condiciones ambientales

Como sistema de riego
Quiero recibir lecturas de temperatura y humedad
Para decidir cuándo regar automáticamente

Criterios de aceptación

Given valores de temperatura y humedad

When los sensores notifican al controlador

Then se evalúa si las condiciones están dentro del rango de riego permitido.

Referencia

riego/sensores/temperatura_reader_task.py

riego/sensores/humedad_reader_task.py

patrones/observer/observable.py

Test: tests/test_riego_control.py

HU-3.2 — Aplicar riego con absorción por tipo de cultivo

Como controlador de riego
Quiero distribuir el agua entre los cultivos
Para simular diferentes formas de absorción según el tipo de planta

Criterios de aceptación

Given una plantación con cultivos de distintos tipos

When se ejecuta el riego

Then cada cultivo absorbe agua según su estrategia de absorción.

Referencia

patrones/strategy/absorcion_agua_strategy.py

patrones/strategy/impl/absorcion_constante_strategy.py

Test: tests/test_riego_control.py

Épica 4 — Reglas de Crecimiento y Estado
HU-4.1 — Aumentar la altura de los árboles después del riego

Como ingeniero forestal
Quiero que los árboles crezcan cada vez que se riegan
Para reflejar el desarrollo del cultivo en el sistema

Criterios de aceptación

Given un cultivo tipo Pino

When se riega

Then su altura aumenta 0.10 m.

Referencia

servicios/cultivos/pino_service.py

HU-4.2 — Cambiar el estado de las hortalizas al crecer

Como horticultor
Quiero que las hortalizas cambien su estado de crecimiento
Para reflejar su evolución a lo largo del tiempo

Criterios de aceptación

Given una lechuga en estado “semilla”

When se riega

Then pasa a estado “creciendo”.

Referencia

servicios/cultivos/lechuga_service.py

Test: tests/test_cultivo_services.py

Épica 5 — Servicios y Estructura (Singleton + Excepciones)
HU-5.1 — Gestionar los servicios con un registro único

Como desarrollador del sistema
Quiero acceder a los servicios desde un único punto compartido
Para mantener coherencia entre las instancias

Criterios de aceptación

Given distintos servicios de cultivo

When se obtiene el CultivoServiceRegistry.instance()

Then todos los módulos comparten la misma instancia (Singleton).

Referencia

servicios/cultivos/cultivo_service_registry.py

Test: tests/test_cultivo_services.py
