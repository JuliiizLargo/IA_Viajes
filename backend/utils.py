from ics import Calendar, Event
from datetime import datetime, timedelta

def itinerary_to_ics(city, start_date, days, plan_text):
    cal = Calendar()
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    for i in range(days):
        e = Event()
        e.name = f"Viaje a {city} - Día {i+1}"
        e.begin = base_date + timedelta(days=i)
        e.description = plan_text
        cal.events.add(e)

    file_path = f"static/itinerary_{city}.ics"
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(cal.serialize_iter())
    return "/" + file_path
