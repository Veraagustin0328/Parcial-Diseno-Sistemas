"""
Archivo integrador generado automaticamente
Directorio: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\strategy\impl
Fecha: 2025-10-21 23:28:07
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\strategy\impl\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ================================================================================

﻿from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
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


# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: C:\Users\veraa\ParcialMendoza\PythonForestal\.\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ================================================================================



