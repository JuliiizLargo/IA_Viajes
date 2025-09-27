from groq_client import ask_groq

def generate_itinerary(city: str, days: int, hotels, flights, places) -> str:
    prompt = f"""
    Eres un agente de viajes profesional. 
    Organiza un itinerario de {days} días en {city}.
    
    Hoteles sugeridos:
    {hotels}

    Vuelos sugeridos:
    {flights}

    Actividades recomendadas:
    {places}

    Devuelve el plan día por día, con horarios aproximados, 
    formato fácil de leer, estilo profesional.
    """
    return ask_groq(prompt)
