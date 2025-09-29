

from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)

@app.route("/api/itinerary", methods=["POST"])
def itinerary():
    try:
        data = request.get_json(force=True)
        city = data.get("city")
        days = int(data.get("days", 0))
        start_date = data.get("start_date")

        if not city or not days or not start_date:
            return jsonify({"error": "Faltan datos: city, days o start_date"}), 400

        # Aquí generas tu itinerario (lógica simulada)
        itinerary_text = f"Itinerario para {city}: {days} días desde {start_date}"

        # Ejemplo de archivo ICS ficticio
        ics_file_url = "/static/itinerary.ics"

        return jsonify({
            "itinerary": itinerary_text,
            "ics_file": ics_file_url
        })

    except Exception as e:
        print("❌ Error en /api/itinerary:", e)
        traceback.print_exc()
        return jsonify({
            "error": "Ocurrió un error interno en el servidor",
            "details": str(e)
        }), 500


@app.route("/api/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        question = data.get("question")

        if not question:
            return jsonify({"error": "La pregunta no puede estar vacía"}), 400

        # Aquí pones la lógica de tu agente (respuesta simulada)
        answer = f"Respuesta automática para: {question}"

        return jsonify({"answer": answer})

    except Exception as e:
        print("❌ Error en /api/ask:", e)
        traceback.print_exc()
        return jsonify({
            "error": "Ocurrió un error interno en el servidor",
            "details": str(e)
        }), 500


# Ruta para verificar que el servidor está vivo
@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})


