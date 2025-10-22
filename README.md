El proyecto Sistema de Gestión Forestal implementa una arquitectura orientada a objetos basada en patrones de diseño para la administración de plantaciones agrícolas y forestales.
El sistema permite crear distintas plantaciones, registrar cultivos y gestionar el riego de forma automatizada a partir de lecturas de sensores de temperatura y humedad. La simulación demuestra cómo cada componente del sistema interactúa siguiendo principios de diseño reutilizable, mantenible y extensible

Patrones de Diseño Implementados

Singleton: asegura que el registro de servicios (CultivoServiceRegistry) mantenga una única instancia en toda la aplicación.

Factory Method: permite crear objetos de cultivos (Pino, Lechuga, Olivo, Zanahoria) a partir de un tipo genérico, facilitando la extensibilidad del sistema.

Observer: modela el sistema de sensores ambientales, donde los controladores de riego se suscriben a eventos de temperatura y humedad para reaccionar en tiempo real.

Strategy: define algoritmos de absorción de agua intercambiables, aplicados de forma dinámica según el tipo de cultivo durante el proceso de riego.