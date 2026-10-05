"""
FastAPI application entry point.

Creates the FastAPI app, registers routers, and configures CORS so the
React frontend can communicate with this API during local development.
"""

from fastapi import FastAPI
from app.api.v1.router import router as v1_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import router
from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging
import logging
from app.core.exceptions import (
    MovieVerseException,
    movieverse_exception_handler,
)

app = FastAPI(
    title="MovieVerse API",
    version="0.1.0",
    debug=settings.debug,
)
app.include_router(v1_router, prefix="/api/v1")
setup_logging()
app.add_exception_handler(
    MovieVerseException,
    movieverse_exception_handler,
)
logger = logging.getLogger(__name__)
logger.info("MovieVerse API started")
app.include_router(v1_router, prefix="/api/v1")

# Allow the React dev server (port 5173) to make requests to this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Routers ────────────────────────────────────────────────────────
app.include_router(health_router)
