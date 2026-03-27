from openai import OpenAI
import os
import random

def get_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Memoria del usuario
memoria = {
    "nombre": None,
    "categoria_favorita": None
}

productos = ["Laptop X200", "Smartphone Pro", "Auriculares Z", "Celulares"]

def recomendar_producto():
    if memoria.get("categoria_favorita"):
        return f"Te recomiendo un producto de tu categoría favorita: {memoria['categoria_favorita']}"
    
    if not productos:
        return "No hay productos disponibles"
    
    return f"Te recomiendo este producto: {random.choice(productos)}"

def consultar_ia(user_input, client):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente de ventas útil y cordial"},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error con la API de OpenAI: {e}"

def agente(user_input, client=None):
    if client is None:
        client = get_client()

    user_input_lower = user_input.lower()

    if "me llamo" in user_input_lower:
        nombre = user_input_lower.split("me llamo")[-1].strip().title()
        memoria["nombre"] = nombre
        return f"¡Encantado de conocerte, {nombre}!"

    if "recomiéndame algo" in user_input_lower or "sugerencia" in user_input_lower:
        return recomendar_producto()

    return consultar_ia(user_input, client)

def chat():
    print("🤖 Agente híbrido iniciado. Escribe 'salir' para terminar.")
    client = get_client()

    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "adiós", "chao"]:
            print("Agente: ¡Hasta luego!")
            break
        respuesta = agente(user_input, client)
        print(f"Agente: {respuesta}")

if __name__ == "__main__":
    chat()