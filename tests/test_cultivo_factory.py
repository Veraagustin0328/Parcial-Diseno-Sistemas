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
