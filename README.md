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


## Overview by Infographics:

### English
![EN](docs/images/api-overview-en.png)

### Português (Brasil)
![PT-BR](docs/images/api-overview-pt-br.png)

### Español (España)
![ES](docs/images/api-overview-es-es.png)


## Initial structure:

```bash
api-engineering-lab/
│
├── README.md
│
├── docs/
│   ├── api-fundamentals.md
│   ├── http-basics.md
│   ├── rest-architecture.md
│   ├── openapi-swagger.md
│   ├── authentication.md
│   ├── versioning.md
│   ├── observability.md
│   ├── grpc.md
│   ├── graphql.md
│   └── interview-notes.md
│
├── diagrams/
│   ├── high-level-architecture.png
│   ├── request-flow.png
│   └── observability-flow.png
│
├── images/
│
├── labs/
│
│   ├── 01-fastapi-basics/
│   ├── 02-rest-crud/
│   ├── 03-openapi-documentation/
│   ├── 04-pydantic-validation/
│   ├── 05-error-handling/
│   ├── 06-authentication/
│   ├── 07-testing/
│   ├── 08-postman/
│   ├── 09-k6-load-testing/
│   ├── 10-observability/
│   ├── 11-webhooks/
│   ├── 12-websockets/
│   ├── 13-graphql/
│   └── 14-grpc/
│
├── postman/
│
├── k6/
│
└── .github/
```

### Questions proposed for each lab:

- How is this API documented?

- How does an external consumer understand the contract?

- How are errors standardized?

- How is authentication applied?

- How do I test it?

- How do I monitor it?

- How do I version it without breaking clients?

- How do I know if the API is slow?

- How do I compare REST with gRPC, GraphQL, or WebSockets?
