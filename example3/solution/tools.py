from pathlib import Path

from strands import tool

HOURS = {
    "Fushimi Inari": "Always open",
    "Kiyomizu-dera": "6:00-18:00",
    "Arashiyama": "Always open",
    "Osaka Castle": "9:00-17:00",
    "Dotonbori": "Always open",
}


@tool
def read_attractions_file(city: str) -> list[str]:
    """Read attractions from data/attractions.txt for a given city."""
    data_path = Path(__file__).parent / "data" / "attractions.txt"
    if not data_path.exists():
        return []

    for line in data_path.read_text().splitlines():
        if "|" not in line:
            continue
        city_name, places = line.split("|", 1)
        if city_name.strip().lower() == city.strip().lower():
            return [p.strip() for p in places.split(",") if p.strip()]
    return []


@tool
def get_hours(place: str) -> str:
    """Return hours for a place."""
    return HOURS.get(place, "Hours unavailable")
