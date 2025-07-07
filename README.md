# Automation Infra Tech Lead Assignment – Test Server

This project simulates a RESTful product API and a Python client interface for automated test scenarios.  


## 🚀 Features

- ✅ **FastAPI** server with clean routing and input validation  
- ✅ **SQLite** for persistent user storage  
- ✅ **Python client** as the interface for automation developers  
- ✅ **Logging** with file and console outputs  
- ✅ **Comprehensive input validation** (ID, phone, non-empty fields)  
- ✅ **Error handling** with meaningful status codes  
- ✅ **Modular design** (routes, models, schemas, DB session)  
- ✅ **Dockerized** for portability  
- ✅ **Test script** to simulate client usage  


## 🧱 Project Structure
```
test_app/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   └── logger.py
├── client/
│   ├── __init__.py
│   └── api_client.py
├── test_client_demo.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

## 🛠️ Setup Instructions

### ✅ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open in browser: http://localhost:8000/docs

### 🐳 Run via Docker
```bash
docker build -t aqua-api .
docker run -d -p 8000:8000 aqua-api
```
Then open in browser: http://localhost:8000/docs

## 🔍 API Endpoints

| Method | Path            | Description             |
|--------|------------------|-------------------------|
| GET    | `/health`        | Health check            |
| POST   | `/users`         | Create new user         |
| GET    | `/users/{id}`    | Get user by ID          |
| GET    | `/users`         | List all user IDs       |

*** Can also be found in Swagger UI: http://localhost:8000/docs

## 🧪 Python Client Demo

File: `test_client_demo.py`

```python
from client.api_client import UserApiClient

client = UserApiClient("http://127.0.0.1:8000")

user = {
  "id": "123456789",
  "name": "Alice",
  "phone": "+972501234567",
  "address": "Tel Aviv"
}

client.create_user(user)
print(client.get_user("123456789"))
```

## 🧠 Design Decisions

- **FastAPI** was chosen for its native validation, OpenAPI documentation, and async support.
- **SQLite** provides a lightweight, zero-config database for local persistence.
- **Python client** abstracts HTTP logic to simplify automated test development.
- **Logging** is configured for both console and file output to track system behavior.
- **Validation** ensures test input quality, stability, and safety.
- **Modular structure** follows clean separation of concerns, aiding scalability and readability.


## 🔧 Future Improvements

| Area         | Suggestion                                                                  |
|--------------|-----------------------------------------------------------------------------|
| Auth         | Add JWT or API key authentication                                           |
| Testing      | Add pytest-based unit and integration tests                                 |
| CI/CD        | Integrate GitHub Actions or Jenkins to automate testing and deployment      |
| DB           | Swap SQLite for PostgreSQL or MySQL in production environments              |
| Logging      | Integrate with centralized logging tools (e.g., Logstash, coralogix etc...) |
| Deployment   | Deploy via Docker to dynamic EC2 or ECS; optionally expose with a domain    |
| Public Access| Set up remote access to API for automated remote test runs                  |
| Client SDK   | Package and publish the Python client as a pip-installable module           |


