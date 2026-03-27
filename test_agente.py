import pytest
from mi_agente import agente, memoria

def test_nombre_usuario():
    respuesta = agente("me llamo Juan")
    assert "Juan" in respuesta
    assert memoria["nombre"] == "Juan"

def test_recomendacion_con_categoria():
    memoria["categoria_favorita"] = "Tecnología"
    respuesta = agente("recomiéndame algo")
    assert "Tecnología" in respuesta

def test_recomendacion_sin_categoria():
    memoria["categoria_favorita"] = None
    respuesta = agente("recomiéndame algo")
    assert "Te recomiendo" in respuesta

def test_input_normal_ia():
    respuesta = agente("Hola, ¿qué vendes?")
    assert isinstance(respuesta, str)

def test_falla_intencional():
    assert 1 == 2  # ❌ siempre falla