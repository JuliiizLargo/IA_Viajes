import os
from groq import Groq

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("❌ GROQ_API_KEY no está configurada en variables de entorno.")

client = Groq(api_key=API_KEY)

def ask_groq(prompt: str) -> str:
    if not prompt:
        return "⚠️ No se recibió un prompt para procesar."
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
 
        return response.choices[0].message["content"] if response.choices else "⚠️ No se generó respuesta."
    except Exception as e:
        return f"⚠️ Error llamando a Groq API: {str(e)}"
