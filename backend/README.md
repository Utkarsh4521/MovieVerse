# MovieVerse Backend

FastAPI backend for the MovieVerse application.

## Running Locally

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Health Check

```
GET http://localhost:8000/health
-> {"status": "ok"}
```

## Structure

```
backend/
-- app/
   -- api/           HTTP route handlers
   -- core/          Configuration and shared dependencies
   -- db/            SQLAlchemy engine and session management
   -- models/        ORM models (domain models added per module)
   -- schemas/       Pydantic request/response schemas
   -- repositories/  Database access layer
   -- services/      Business logic layer
   -- main.py        Application entry point
-- tests/
-- requirements.txt
-- Dockerfile
```