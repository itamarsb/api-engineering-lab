"""Simulated weather data used by the Weather API."""

WEATHER_DATA: dict[str, dict[str, object]] = {
    "rio-grande": {
        "city": "Rio Grande",
        "state": "RS",
        "country": "Brazil",
        "temperature_c": 16.5,
        "condition": "Partly cloudy",
        "humidity_percent": 82,
        "wind_speed_kmh": 21.0,
    },
    "porto-alegre": {
        "city": "Porto Alegre",
        "state": "RS",
        "country": "Brazil",
        "temperature_c": 19.8,
        "condition": "Cloudy",
        "humidity_percent": 76,
        "wind_speed_kmh": 13.0,
    },
    "orlando": {
        "city": "Orlando",
        "state": "FL",
        "country": "United States",
        "temperature_c": 30.2,
        "condition": "Sunny",
        "humidity_percent": 68,
        "wind_speed_kmh": 11.0,
    },
    "tampa": {
        "city": "Tampa",
        "state": "FL",
        "country": "United States",
        "temperature_c": 31.0,
        "condition": "Scattered clouds",
        "humidity_percent": 72,
        "wind_speed_kmh": 15.0,
    },
}
