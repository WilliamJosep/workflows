import pytest
from mi_agente import agente, memoria

def test_input_normal_ia(monkeypatch):

    class MockResponse:
        class Choice:
            class Message:
                content = "Respuesta simulada"
            message = Message()
        choices = [Choice()]

    def mock_create(*args, **kwargs):
        return MockResponse()

    from mi_agente import client
    monkeypatch.setattr(client.chat.completions, "create", mock_create)

    respuesta = agente("Hola")
    assert respuesta == "Respuesta simulada"