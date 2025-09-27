import os
import requests

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")
BASE_URL = "https://serpapi.com/search.json"

def search_hotels(city: str):
    params = {"engine": "google_hotels", "q": city, "api_key": SERP_API_KEY}
    r = requests.get(BASE_URL, params=params)
    return r.json()

def search_flights(origin: str, destination: str, date: str):
    params = {
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        "outbound_date": date,
        "api_key": SERP_API_KEY
    }
    r = requests.get(BASE_URL, params=params)
    return r.json()

def search_places(city: str):
    params = {"engine": "google_maps", "q": f"Atracciones turísticas en {city}", "api_key": SERP_API_KEY}
    r = requests.get(BASE_URL, params=params)
    return r.json()
