from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.domain.exceptions import HTTPException


def create_app():
    app = FastAPI()
# Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
        allow_credentials=True,
        allow_methods=["GET","POST","PUT","DELETE"],  # Allows all methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )
    @app.exception_handler(HTTPException)
    async def exception_handler(_, exception: HTTPException):
        return JSONResponse(
            status_code=exception.status_code,
            content={"error_body": {"title": exception.title, "message": exception.message}}
        )


    return app