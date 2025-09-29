

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# ✅ Comprobamos claves de API al inicio y avisamos si faltan
GROQ_KEY = os.getenv("GROQ_API_KEY")
SERP_KEY = os.getenv("SERPAPI_API_KEY")
if not GROQ_KEY:
    print("⚠️ Advertencia: GROQ_API_KEY no está configurada. /api/ask fallará.")
if not SERP_KEY:
    print("⚠️ Advertencia: SERPAPI_API_KEY no está configurada. /api/itinerary devolverá datos vacíos.")

@app.route("/api/itinerary", methods=["POST"])
def api_itinerary():
    try:
        data = request.json or {}
        city = data.get("city")
        if not city:
            return jsonify({"error": "Falta el destino (city)."}), 400

        days = int(data.get("days", 3))
        start_date = data.get("start_date", "2025-10-01")

        from serp_client import search_hotels, search_flights, search_places
        hotels = search_hotels(city) if SERP_KEY else {}
        flights = search_flights("BOG", city, start_date) if SERP_KEY else {}
        places = search_places(city) if SERP_KEY else {}

        from itinerary import generate_itinerary
        itinerary_text = generate_itinerary(city, days, hotels, flights, places)

        from utils import itinerary_to_ics
        ics_file = itinerary_to_ics(city, start_date, days, itinerary_text)

        return jsonify({"itinerary": itinerary_text, "ics_file": ics_file})

    except Exception as e:
        # ✅ SIEMPRE devolvemos JSON en caso de error
        return jsonify({"error": f"Error generando itinerario: {str(e)}"}), 500


@app.route("/api/ask", methods=["POST"])
def api_ask():
    try:
        from groq_client import ask_groq
        data = request.json or {}
        question = data.get("question", "").strip()
        if not question:
            return jsonify({"error": "Pregunta vacía."}), 400

        answer = ask_groq(question)
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": f"Error en IA: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)

