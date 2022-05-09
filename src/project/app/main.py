from fastapi import FastAPI

from .api.v1 import users


app = FastAPI(
    title="First FastAPI application",
    docs_url='/api/openapi/',
    openapi_url='/api/openapi.json',
)


app.include_router(users.router, prefix='/api/v1/users', tags=["User"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
