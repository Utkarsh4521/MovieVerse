"""
Health check endpoint.

GET /health
    Returns {"status": "ok"} when the application is running.
    Used by Docker, load balancers, and monitoring tools to verify liveness.
"""

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()


@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "ok"}
