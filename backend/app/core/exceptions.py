from fastapi import Request
from fastapi.responses import JSONResponse


class MovieVerseException(Exception):
    """Base exception for MovieVerse."""


async def movieverse_exception_handler(
    request: Request,
    exc: MovieVerseException,
):
    return JSONResponse(
        status_code=400,
        content={
            "detail": str(exc),
        },
    )