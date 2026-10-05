# MovieVerse

A full-stack web application for discovering and tracking movies, anime, and series.

## Tech Stack

| Layer      | Technology                         |
|------------|------------------------------------|
| Frontend   | React, Vite, JavaScript, Tailwind  |
| Backend    | Python, FastAPI, SQLAlchemy        |
| Database   | PostgreSQL                         |
| Infra      | Docker, Docker Compose             |

## Project Structure

    MovieVerse/
    -- frontend/     # React + Vite application
    -- backend/      # FastAPI application
    -- .env          # Local development secrets (git-ignored)
    -- .env.example  # Variable template (safe to commit)
    -- docker-compose.yml

## Getting Started

### Prerequisites
- Node.js v18+
- Python 3.12+
- Docker + Docker Compose

### Local Development

**Frontend**
    cd frontend && npm install && npm run dev

**Backend**
    cd backend
    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

**Docker (full stack)**
    docker compose up --build

## Health Check

    GET http://localhost:8000/health
