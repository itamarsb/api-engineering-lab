# Lab 01 — Weather API

### Scope of this first version

We will implement four endpoints:

```http
GET /
GET /health
GET /weather
GET /weather/{city}
```

They will demonstrate:

- creating a FastAPI application;
- HTTP GET operations;
- JSON responses;
- path parameters;
- query parameters;
- HTTP status codes;
- handling non-existent cities;
- automatic documentation with Swagger UI and ReDoc;
- local execution;
- manual testing via browser, Swagger, PowerShell, and Postman.

FastAPI automatically distinguishes between parameters present in the path and those received in the query string. Type annotations are also used for conversion, validation, and OpenAPI contract generation.

---

## 1. Laboratory structure

Within the repository, we will create:

```text
api-engineering-lab/
│
├── labs/
│   └── 01-weather-api/
│       ├── app/
│       │   ├── __init__.py
│       │   ├── data.py
│       │   └── main.py
│       │
│       ├── docs/
│       │   └── images/
│       │
│       ├── .gitignore
│       ├── README.md
│       └── requirements.txt
│
└── README.md
```

For Lab 01, this structure offers a good balance: it is small enough to grasp (especially if you are a beginner following the tutorial in this repository), yet it avoids concentrating the entire project into a single file.

---

## 2. Create the lab folder

In the VS Code integrated terminal, run the following from the repository root:

### PowerShell

```powershell
mkdir labs\01-weather-api
mkdir labs\01-weather-api\app
mkdir labs\01-weather-api\docs
mkdir labs\01-weather-api\docs\images

New-Item labs\01-weather-api\app\__init__.py -ItemType File
New-Item labs\01-weather-api\app\data.py -ItemType File
New-Item labs\01-weather-api\app\main.py -ItemType File
New-Item labs\01-weather-api\requirements.txt -ItemType File
New-Item labs\01-weather-api\.gitignore -ItemType File
New-Item labs\01-weather-api\README.md -ItemType File

cd labs\01-weather-api
```

It is also possible to create these folders manually using the VS Code Explorer.

![Lab01](docs/images/Lab01_Clipboard_07-24-2026_01.jpg)

AND

![Lab01](docs/images/Lab01_Clipboard_07-24-2026_02.jpg)


---


## 3. Create the virtual environment

Inside `labs/01-weather-api`, run:

```powershell
python -m venv .venv
```

The `venv` creates an isolated environment so that the lab's dependencies do not mix with global packages or other Python projects. The name `.venv` is a common convention for this directory.

![Lab01](docs/images/Lab01_Clipboard_07-24-2026_03.jpg)


Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

When active, the terminal should display something similar to:

```powershell
(.venv) PS C:\...\api-engineering-lab\labs\01-weather-api>
```

However, if PowerShell blocks the activation, run it only for the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then, try again:

```powershell
.venv\Scripts\Activate.ps1
```

![Lab01](docs/images/Lab01_Clipboard_07-24-2026_04.jpg)


---


## 4. Install FastAPI

Populate the `requirements.txt` file with:

```text
fastapi[standard]
```

![Lab01](docs/images/Lab01_Clipboard_07-24-2026_05.jpg)


Then run:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The `fastapi[standard]` installation includes the standard dependencies required to run the application and provides the FastAPI CLI. Current documentation recommends working within a virtual environment and running the application in development mode using `fastapi dev`.


![Lab01](docs/images/Lab01_Clipboard_07-24-2026_06.jpg)


Once we confirm that everything is working, we can pin the installed versions:

```powershell
pip freeze > requirements.txt
```

This makes future execution more reproducible. The FastAPI documentation itself recommends pinning a version that has been validated by the project, especially before evolving or publishing the application.

![Lab01](docs/images/Lab01_Clipboard_07-24-2026_07.jpg)


> [!TIP]
> **Note:**
>
> If you are new to FastAPI, I suggest you take some time to review the official FastAPI documentation (at the link below), as there is no better material for learning any technology than the official documentation provided by the developers themselves:
>
> https://fastapi.tiangolo.com/
> 


---


## 5. Create the simulated weather data

In the file:

```text
app/data.py
```

add:

```python
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
```

This data is deliberately simulated. We will not need:

- an API key;
- registration with an external service;
- an internet connection;
- handling of request limits;
- third-party dependencies.

The goal of this lab is to learn the structure and behavior of an API, not to integrate a real weather provider. That type of integration will be demonstrated later in another lab.


![Lab01](docs/images/Lab01_Clipboard_07-24-2026_08.jpg)


### What this code already demonstrates:

The endpoint:

```http
GET /weather/{city}
```

uses `city` as path parameter:

```http
GET /weather/orlando
```

While `unit` is a query parameter:

```http
GET /weather/orlando?unit=fahrenheit
```

FastAPI identifies these parameters based on the route declaration and the function signature. It also applies validations and includes the information in the OpenAPI documentation.


---


## 7. Create the .gitignore

In the file:

```text
.gitignore
```

add:

```gitignore
# Virtual environment
.venv/
venv/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Test and coverage artifacts
.pytest_cache/
.coverage
htmlcov/

# Environment variables
.env

# IDE files
.vscode/
.idea/

# Operating system files
.DS_Store
Thumbs.db
```

The `.venv` folder should not be pushed to GitHub. The repository will store dependencies in `requirements.txt`, not a full copy of the Python environment.


