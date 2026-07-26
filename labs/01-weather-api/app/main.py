"""Lab 01 - Weather API.

A small FastAPI application created to demonstrate HTTP, REST, JSON,
routing, path parameters, query parameters and automatic API documentation.
"""

from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Path, Query, status

from app.data import WEATHER_DATA


app = FastAPI(
    title="Weather API",
    description=(
        "An introductory REST API that returns simulated weather data "
        "for selected cities."
    ),
    version="1.0.0",
    contact={
        "name": "Itamar de Sá Britto Júnior",
        "url": "https://github.com/itamarsb",
    },
    license_info={
        "name": "MIT",
    },
)


def normalize_city(city: str) -> str:
    """Convert a city name into the key format used by the dataset."""

    return city.strip().lower().replace(" ", "-")


@app.get(
    "/",
    tags=["General"],
    summary="Display API information",
)
async def root() -> dict[str, str]:
    """Return basic information and documentation links."""

    return {
        "name": "Weather API",
        "version": "1.0.0",
        "description": "Simulated weather data for API learning.",
        "documentation": "/docs",
        "alternative_documentation": "/redoc",
        "health_check": "/health",
    }


@app.get(
    "/health",
    tags=["General"],
    summary="Check API availability",
)
async def health_check() -> dict[str, str]:
    """Return the current operational status of the API."""

    return {
        "status": "healthy",
        "service": "weather-api",
        "version": "1.0.0",
    }


@app.get(
    "/weather",
    tags=["Weather"],
    summary="List available weather records",
)
async def list_weather(
    unit: Annotated[
        Literal["celsius", "fahrenheit"],
        Query(description="Temperature unit used in the response"),
    ] = "celsius",
) -> dict[str, object]:
    """Return weather information for all available cities."""

    records = [
        convert_temperature(record, unit)
        for record in WEATHER_DATA.values()
    ]

    return {
        "unit": unit,
        "count": len(records),
        "data": records,
    }


@app.get(
    "/weather/{city}",
    tags=["Weather"],
    summary="Get weather by city",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "The requested city was not found."
        }
    },
)
async def get_weather_by_city(
    city: Annotated[
        str,
        Path(
            min_length=2,
            max_length=80,
            description="City name, such as Rio Grande, Orlando or Tampa",
            examples=["Rio Grande"],
        ),
    ],
    unit: Annotated[
        Literal["celsius", "fahrenheit"],
        Query(description="Temperature unit used in the response"),
    ] = "celsius",
) -> dict[str, object]:
    """Return simulated weather information for one city."""

    city_key = normalize_city(city)
    weather = WEATHER_DATA.get(city_key)

    if weather is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "city_not_found",
                "message": f"Weather data is not available for '{city}'.",
                "available_cities": [
                    item["city"] for item in WEATHER_DATA.values()
                ],
            },
        )

    return {
        "unit": unit,
        "data": convert_temperature(weather, unit),
    }


def convert_temperature(
    weather: dict[str, object],
    unit: Literal["celsius", "fahrenheit"],
) -> dict[str, object]:
    """Return a copy of a weather record using the selected unit."""

    result = dict(weather)
    temperature_c = float(result.pop("temperature_c"))

    if unit == "fahrenheit":
        result["temperature"] = round((temperature_c * 9 / 5) + 32, 1)
        result["temperature_unit"] = "°F"
    else:
        result["temperature"] = temperature_c
        result["temperature_unit"] = "°C"

    return result
