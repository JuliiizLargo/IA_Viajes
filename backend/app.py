import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from serp_client import search_hotels, search_flights, search_places
from itinerary import generate_itinerary
from utils import itinerary_to_ics

load_dotenv()
app = Flask(__name__)

@app.route("/api/itinerary", methods=["POST"])
def api_itinerary():
    try:
        data = request.json or {}
        city = data.get("city")
        if not city:
            return jsonify({"error": "Falta el destino (city)."}), 400

        days = int(data.get("days", 3))
        start_date = data.get("start_date", "2025-10-01")

        
        hotels = search_hotels(city)
        flights = search_flights("BOG", city, start_date)
        places = search_places(city)

        itinerary_text = generate_itinerary(city, days, hotels, flights, places)
        ics_file = itinerary_to_ics(city, start_date, days, itinerary_text)

        return jsonify({"itinerary": itinerary_text, "ics_file": ics_file})

    except Exception as e:
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
