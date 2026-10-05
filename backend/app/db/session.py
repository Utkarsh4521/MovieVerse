"""
Database engine and session management.

engine       -- SQLAlchemy connection pool to PostgreSQL
SessionLocal -- factory for creating individual database sessions

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.database_url,
    # Keep one connection alive in the pool for lightweight dev usage.
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
# dependency usage ke liye ye function banaya hai, jisse hum apne endpoints me use karenge fastapi me 
def get_db(): 
    db = SessionLocal()
    try:
        yield db  # fastapi temporary session provide karega, aur ye session close ho jayega jab request complete ho jayega
    finally:
        db.close()