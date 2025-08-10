import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

def geocode_location(name, country=None):
    """Return latitude and longitude for a given name and country using Nominatim."""
    query = f"{name}, {country}" if country else name
    try:
        response = requests.get(
            NOMINATIM_URL,
            params={"q": query, "format": "json", "limit": 1},
            headers={"User-Agent": "travel-planner"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except requests.RequestException:
        pass
    return None, None
