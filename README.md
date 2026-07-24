# API Engineering Lab — Learning Roadmap

This roadmap presents a progressive journey through API fundamentals, professional development, testing, multiple frameworks, delivery practices and complete API projects.

Each lab builds a practical API for a different business scenario, introducing new concepts and technologies while reinforcing previously acquired skills.

## Overall Progress

**Completed:** 0 / 18 Labs

### Status Legend

- ⬜ Planned
- 🟨 In Progress
- ✅ Completed

### Level Legend

- 🟢 Fundamentals
- 🟡 Intermediate
- 🟠 Testing
- 🔵 Multi-Framework
- 🔴 Delivery
- 🟣 Consolidated Project


---

## 🟢 Phase 1 — API Fundamentals

Build a solid foundation in HTTP, REST, JSON, resource modeling, validation and error handling.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 01 | 🟢 | Weather API | Public Weather Service | HTTP, REST, JSON, Routing, Query Parameters | Python, FastAPI | REST Design, Routing, Responses |
| ⬜ | 02 | 🟢 | Library Management API | University Library | CRUD, Resources, HTTP Methods, Status Codes | Python, FastAPI | Resource Modeling, CRUD Operations |
| ⬜ | 03 | 🟢 | Inventory API | Retail Inventory | Schemas, Validation, Error Handling | Python, FastAPI, Pydantic | Input Validation, Standardized Errors |

### Planned Content

### Lab 01 — Weather API

An introductory API that initially does not rely on an external weather service. It will accept a city name and return simulated data in JSON format. The goal is to learn API structure, create routes, and work with parameters.

Possible endpoints:

```text
GET /
GET /health
GET /weather
GET /weather/{city}
```

---

## 🟡 Phase 2 — Professional API Development

Develop APIs with authentication, persistence, relational data and advanced resource queries.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 04 | 🟡 | Authentication API | SaaS Platform | Password Hashing, JWT, Protected Routes, Authorization | Python, FastAPI, JWT | Authentication, Route Protection |
| ⬜ | 05 | 🟡 | Blog Platform API | Content Publishing Platform | Persistence, ORM, Relationships, Data Modeling | FastAPI, SQLite, SQLAlchemy | Database Integration, Relational Modeling |
| ⬜ | 06 | 🟡 | E-commerce Catalog API | Online Store | Pagination, Filtering, Sorting, Search | FastAPI, SQLAlchemy | Query Design, Collection Endpoints |


---

## 🟠 Phase 3 — API Testing with Postman

Create organized test collections, environments, assertions and automated API test executions.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 07 | 🟠 | Movie Catalog API | Streaming Catalog | Requests, Collections, Environments, Variables | Postman, FastAPI | Manual API Testing, Test Organization |
| ⬜ | 08 | 🟠 | Task Management API | Team Productivity Platform | Assertions, Test Scripts, Dynamic Variables | Postman, JavaScript | Automated Functional Testing |
| ⬜ | 09 | 🟠 | Hotel Booking API | Hotel Reservation Platform | Authentication Flow, Collection Runner, Newman | Postman, Newman, JavaScript | End-to-End API Testing |


---

## 🔵 Phase 4 — Multi-Framework API Development

Apply the same API engineering principles using different languages, frameworks and architectural styles.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 10 | 🔵 | Currency Exchange API | Financial Utility Service | External APIs, Async Requests, Error Mapping | Python, FastAPI, HTTPX | External API Integration |
| ⬜ | 11 | 🔵 | Flight Search API | Airline Search Platform | Flask Routing, Blueprints, Serialization | Python, Flask | Flask API Development |
| ⬜ | 12 | 🔵 | Student Management API | Education Platform | Express Routing, Middleware, Controllers | JavaScript, Node.js, Express | JavaScript API Development |
| ⬜ | 13 | 🔵 | Healthcare Appointment API | Appointment Scheduling Platform | TypeScript, Modules, Services, DTOs | TypeScript, NestJS | Structured Backend Development |


---

## 🔴 Phase 5 — API Delivery Basics

Package APIs into containers and automate their basic quality and testing workflows.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 14 | 🔴 | File Storage API | Document Management Service | File Upload, Validation, Download, Metadata | Python, FastAPI | File Handling, Content Validation |
| ⬜ | 15 | 🔴 | Notification API | Notification Service | Environment Variables, Dockerfile, Containers | JavaScript, Express, Docker | API Containerization |
| ⬜ | 16 | 🔴 | Payment Simulation API | Payment Sandbox | Automated Tests, Linting, CI Workflow | GitHub Actions, Postman, Newman | Continuous Integration |


---

## 🟣 Phase 6 — Consolidated API Projects

Consolidate API design, development, persistence, authentication and testing in complete portfolio projects.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 17 | 🟣 | IoT Telemetry API | Sensor Data Collection | Data Ingestion, Timestamps, Filtering, Aggregation | Python, FastAPI, SQLite | Telemetry API Design |
| ⬜ | 18 | 🟣 | Service Desk API | IT Support Management | Authentication, CRUD, Roles, Persistence, Testing | FastAPI or NestJS, Database, Postman | Complete API Lifecycle |



---

## Learning Journey

```text
API Fundamentals
        │
        ▼
Professional API Development
        │
        ▼
API Testing with Postman
        │
        ▼
Multi-Framework Development
        │
        ▼
API Delivery Basics
        │
        ▼
Consolidated API Projects

```

---


## Main Technologies

### Languages
- Python
- JavaScript
- TypeScript

### Frameworks
- FastAPI
- Flask
- Express
- NestJS

### API Design and Documentation
- HTTP
- REST
- JSON
- OpenAPI
- Swagger UI

### Testing
- Postman
- Newman
- JavaScript Test Scripts

### Data and Persistence
- SQLite
- PostgreSQL
- SQLAlchemy

### Delivery
- Docker
- GitHub Actions

---



## Initial directory structure

This structure should evolve as the labs and tutorials are developed.

```text
api-engineering-lab/
│
├── README.md
├── LICENSE
│
├── labs/
│   ├── 01-weather-api/
│   ├── 02-library-management-api/
│   ├── 03-inventory-api/
│   ├── 04-authentication-api/
│   ├── 05-blog-platform-api/
│   ├── 06-ecommerce-catalog-api/
│   ├── 07-movie-catalog-api/
│   ├── 08-task-management-api/
│   ├── 09-hotel-booking-api/
│   ├── 10-currency-exchange-api/
│   ├── 11-flight-search-api/
│   ├── 12-student-management-api/
│   ├── 13-healthcare-appointment-api/
│   ├── 14-file-storage-api/
│   ├── 15-notification-api/
│   ├── 16-payment-simulation-api/
│   ├── 17-iot-telemetry-api/
│   └── 18-service-desk-api/
│
├── postman/
│   ├── collections/
│   └── environments/
│
├── docs/
│   ├── api-fundamentals/
│   └── images/
│
└── .github/
    └── workflows/
```

---

## Overview by Infographics:

### English
![EN](docs/images/api-overview-en.png)

### Português (Brasil)
![PT-BR](docs/images/api-overview-pt-br.png)

### Español (España)
![ES](docs/images/api-overview-es-es.png)


