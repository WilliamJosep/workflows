from openai import OpenAI
import os

# Configurar tu API key desde variable de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEYsk-proj-KL2cs9X2esaQ-gTN1x9pNW2TGzMiDdBtAEVnUPVuzzsIEzdTGL3MJBjRSfnb4QuzH_Z40-3BNyT3BlbkFJrJrz2k67bKfn4bwKFOxombSk_wHI5A8IZ4Zups42t0Xg83sV3PGIa4H5F2onjCmXBK6fJOoh8A"))

# Memoria del usuario
memoria = {
    "nombre": None,
    "categoria_favorita": None
}

# Productos para reglas locales
productos = ["Laptop X200", "Smartphone Pro", "Auriculares Z"]

def agente(user_input):
    user_input_lower = user_input.lower()

    # ===== Reglas locales =====
    # Recordar nombre
    if "me llamo" in user_input_lower:
        nombre = user_input_lower.split("me llamo")[-1].strip().title()
        memoria["nombre"] = nombre
        return f"¡Encantado de conocerte, {nombre}!"

    # Recomendar productos si mencionan categoría favorita
    if "recomiéndame algo" in user_input_lower or "sugerencia" in user_input_lower:
        if memoria.get("categoria_favorita"):
            return f"Te recomiendo un producto de tu categoría favorita: {memoria['categoria_favorita']}"
        else:
            producto = random.choice(productos)
            return f"Te recomiendo este producto: {producto}"

    # ===== Usar IA para el resto =====
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

# Chat interactivo
def chat():
    print("🤖 Agente híbrido iniciado. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "adiós", "chao"]:
            print("Agente: ¡Hasta luego!")
            break
        respuesta = agente(user_input)
        print(f"Agente: {respuesta}")

if __name__ == "__main__":
    chat()