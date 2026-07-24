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

### Lab 02 — Library Management API

First complete CRUD. It will allow for registering, querying, updating, and removing books.

Possible endpoints:

```text
GET    /books
GET    /books/{book_id}
POST   /books
PUT    /books/{book_id}
PATCH  /books/{book_id}
DELETE /books/{book_id}
```

### Lab 03 — Inventory API

API for product and inventory management. The focus will be on data validation, business rules, and consistent error responses.

Validation examples:

- price greater than zero;
- non-negative quantity;
- mandatory and unique SKU;
- non-existent product;
- insufficient stock.


---

## 🟡 Phase 2 — Professional API Development

Develop APIs with authentication, persistence, relational data and advanced resource queries.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 04 | 🟡 | Authentication API | SaaS Platform | Password Hashing, JWT, Protected Routes, Authorization | Python, FastAPI, JWT | Authentication, Route Protection |
| ⬜ | 05 | 🟡 | Blog Platform API | Content Publishing Platform | Persistence, ORM, Relationships, Data Modeling | FastAPI, SQLite, SQLAlchemy | Database Integration, Relational Modeling |
| ⬜ | 06 | 🟡 | E-commerce Catalog API | Online Store | Pagination, Filtering, Sorting, Search | FastAPI, SQLAlchemy | Query Design, Collection Endpoints |


### Planned content

### Lab 04 — Authentication API

Will allow creating users, logging in, and accessing protected routes.

Possible endpoints:

```text
POST /auth/register
POST /auth/login
GET  /auth/me
GET  /admin/users
```

Key concepts:

- secure password storage;
- password hashing;
- JWT generation;
- Bearer Token;
- authenticated user;
- basic role-based permissions.


### Lab 05 — Blog Platform API

The first project featuring actual data persistence. We will use SQLite to keep the lab simple, portable, and easy to run.

Features:

```text
/users
/posts
/comments
/categories
```

Possible relationships:

```text
User 1 ─── N Posts
Post 1 ─── N Comments
Category N ─── N Posts
```

### Lab 06 — E-commerce Catalog API

A catalog API with endpoints that handle larger datasets.

Examples:

```text
GET /products?page=1&limit=10
GET /products?category=electronics
GET /products?min_price=100&max_price=1000
GET /products?sort=price&order=asc
GET /products?search=notebook
```

---

## 🟠 Phase 3 — API Testing with Postman

Create organized test collections, environments, assertions and automated API test executions.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 07 | 🟠 | Movie Catalog API | Streaming Catalog | Requests, Collections, Environments, Variables | Postman, FastAPI | Manual API Testing, Test Organization |
| ⬜ | 08 | 🟠 | Task Management API | Team Productivity Platform | Assertions, Test Scripts, Dynamic Variables | Postman, JavaScript | Automated Functional Testing |
| ⬜ | 09 | 🟠 | Hotel Booking API | Hotel Reservation Platform | Authentication Flow, Collection Runner, Newman | Postman, Newman, JavaScript | End-to-End API Testing |


### Planned content

### Lab 07 — Movie Catalog API

The focus will be on creating and organizing a Postman collection.

The collection may contain:

```text
Health Check
Movies
Genres
Directors
Search
```

The following will be used:

- environments;
- base URL;
- collection variables;
- query parameters;
- headers;
- request body;
- response examples;
- collection documentation.


### Lab 08 — Task Management API

This lab introduces automated tests written in JavaScript within Postman.

Examples:

```JavaScript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response contains task ID", function () {
    const response = pm.response.json();
    pm.expect(response).to.have.property("id");
});
```

We will also have:

- dynamic ID capture;
- request chaining;
- creation and removal of test data;
- header validation;
- type validation;
- positive and negative tests.


### Lab 09 — Hotel Booking API

It will represent a complete business flow:

```text
Register User
      ↓
Login
      ↓
Search Rooms
      ↓
Create Booking
      ↓
Get Booking
      ↓
Cancel Booking
```

The collection will be executed by the Postman Collection Runner and by Newman in the terminal.



---

## 🔵 Phase 4 — Multi-Framework API Development

Apply the same API engineering principles using different languages, frameworks and architectural styles.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 10 | 🔵 | Currency Exchange API | Financial Utility Service | External APIs, Async Requests, Error Mapping | Python, FastAPI, HTTPX | External API Integration |
| ⬜ | 11 | 🔵 | Flight Search API | Airline Search Platform | Flask Routing, Blueprints, Serialization | Python, Flask | Flask API Development |
| ⬜ | 12 | 🔵 | Student Management API | Education Platform | Express Routing, Middleware, Controllers | JavaScript, Node.js, Express | JavaScript API Development |
| ⬜ | 13 | 🔵 | Healthcare Appointment API | Appointment Scheduling Platform | TypeScript, Modules, Services, DTOs | TypeScript, NestJS | Structured Backend Development |


### Planned content

### Lab 10 — Currency Exchange API

You will consume a public currency exchange API and provide a custom interface for conversions.

Possible endpoints:

```text
GET /currencies
GET /rates/{base_currency}
GET /convert?from=USD&to=BRL&amount=100
```

Concepts:

- external API consumption;
- asynchronous HTTP client;
- timeouts;
- handling unavailability;
- mapping external errors;
- currency and value validation.


### Lab 11 — Flight Search API

First API with Flask.

Possible features:

```text
/airports
/flights
/routes
/search
```

The lab will cover:

- application factory;
- blueprints;
- configuration;
- serialization;
- error handling;
- differences between Flask and FastAPI.


### Lab 12 — Student Management API

First API using JavaScript and Node.js.

Suggested structure:

```text
src/
├── controllers/
├── routes/
├── services/
├── middlewares/
├── models/
└── app.js
```

Concepts:

- routes;
- controllers;
- middleware;
- validation;
- centralized error handling;
- asynchronous programming.


### Lab 13 — Healthcare Appointment API

First API using TypeScript and NestJS.

Features:

```text
/patients
/doctors
/specialties
/appointments
```

The lab will demonstrate:

- modules;
- controllers;
- providers;
- services;
- DTOs;
- decorators;
- dependency injection;
- validation with TypeScript.

The project is educational and will not handle real medical data.



---

## 🔴 Phase 5 — API Delivery Basics

Package APIs into containers and automate their basic quality and testing workflows.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 14 | 🔴 | File Storage API | Document Management Service | File Upload, Validation, Download, Metadata | Python, FastAPI | File Handling, Content Validation |
| ⬜ | 15 | 🔴 | Notification API | Notification Service | Environment Variables, Dockerfile, Containers | JavaScript, Express, Docker | API Containerization |
| ⬜ | 16 | 🔴 | Payment Simulation API | Payment Sandbox | Automated Tests, Linting, CI Workflow | GitHub Actions, Postman, Newman | Continuous Integration |


### Planned content

### Lab 14 — File Storage API

It will allow uploading, querying, and downloading files.

Possible endpoints:

```text
POST   /files
GET    /files
GET    /files/{file_id}
GET    /files/{file_id}/download
DELETE /files/{file_id}
```

Validations:

- allowed extension;
- MIME type;
- maximum size;
- safe name;
- non-existent file;
- metadata.


### Lab 15 — Notification API

Express API to simulate sending notifications.

Possible types:

```text
email
sms
push
```

There will be no need to use paid providers. Sending can be simulated and logged locally.

The objectives are:

- configuration via environment variables;
- creation of a `Dockerfile`;
- image creation;
- container execution;
- port exposure;
- optional log persistence.


### Lab 16 — Payment Simulation API

An educational sandbox for simulating payment operations without processing real money.

Supported operations:

```text
POST /payments
GET  /payments/{payment_id}
POST /payments/{payment_id}/confirm
POST /payments/{payment_id}/cancel
POST /payments/{payment_id}/refund
```

The pipeline will be able to execute:

```text
Install Dependencies
        ↓
Lint
        ↓
Start API
        ↓
Run Newman Tests
        ↓
Publish Test Result
```



---

## 🟣 Phase 6 — Consolidated API Projects

Consolidate API design, development, persistence, authentication and testing in complete portfolio projects.

| Status | Lab | Level | API Project | Business Scenario | Main Concepts | Technologies | Skills Demonstrated |
|:---:|:---:|:---:|---|---|---|---|---|
| ⬜ | 17 | 🟣 | IoT Telemetry API | Sensor Data Collection | Data Ingestion, Timestamps, Filtering, Aggregation | Python, FastAPI, SQLite | Telemetry API Design |
| ⬜ | 18 | 🟣 | Service Desk API | IT Support Management | Authentication, CRUD, Roles, Persistence, Testing | FastAPI or NestJS, Database, Postman | Complete API Lifecycle |


### Planned content

### Lab 17 — IoT Telemetry API

You will receive simulated sensor data.

Payload example:

```json
{
  "device_id": "sensor-001",
  "temperature": 24.7,
  "humidity": 71.2,
  "timestamp": "2026-07-23T18:30:00Z"
}
```

Possible endpoints:

```text
POST /telemetry
GET  /telemetry
GET  /telemetry/{device_id}
GET  /telemetry/{device_id}/latest
GET  /telemetry/{device_id}/summary
```

Concepts:

- timestamps;
- data ingestion;
- time-range filters;
- grouping;
- calculation of minimum, maximum, and average;
- device validation;
- contract documentation.


### Lab 18 — Service Desk API

This will be the final and most comprehensive project in the repository.

Features:

```text
/users
/auth
/tickets
/categories
/priorities
/statuses
/comments
```

Possible profiles:

```text
Requester
Technician
Administrator
```

Features:

- user creation;
- login;
- ticket creation;
- technician assignment;
- priority modification;
- status updates;
- comments;
- basic history;
- filters;
- pagination;
- role-based authorization;
- OpenAPI documentation;
- Postman collection;
- tests with Newman;
- well-documented local execution.



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


## Core Principles

Every lab follows these principles:

- Practical and business-oriented API development;
- Clear REST and HTTP semantics;
- Consistent request and response contracts;
- Input validation and standardized error handling;
- OpenAPI documentation;
- Postman-based API testing;
- Progressive use of Python, JavaScript and TypeScript;
- Simple and reproducible local execution;
- Clear technical documentation;
- Portfolio-oriented delivery.



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


