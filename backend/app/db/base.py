"""
SQLAlchemy declarative base.

All ORM models will inherit from Base.
No domain models are created here yet — this file only establishes
the shared metadata object that SQLAlchemy uses.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass