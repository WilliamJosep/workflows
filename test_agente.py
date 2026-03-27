from mi_agente import agente, memoria

def test_nombre_usuario():
    respuesta = agente("me llamo William", client=None)
    assert "William" in respuesta
    assert memoria["nombre"] == "William"

def test_recomendacion():
    memoria["categoria_favorita"] = "Tecnología"
    respuesta = agente("recomiéndame algo", client=None)
    assert "Tecnología" in respuesta

def test_recomendacion_sin_categoria():
    memoria["categoria_favorita"] = None
    respuesta = agente("recomiéndame algo", client=None)
    assert "Te recomiendo" in respuesta

def test_input_normal_ia():

    class MockClient:
        class chat:
            class completions:
                @staticmethod
                def create(*args, **kwargs):
                    class R:
                        class Choice:
                            class Message:
                                content = "Respuesta simulada"
                            message = Message()
                        choices = [Choice()]
                    return R()

    respuesta = agente("Hola", client=MockClient())

    assert respuesta == "Respuesta simulada"