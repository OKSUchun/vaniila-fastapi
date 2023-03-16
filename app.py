from db_connection import exec_query
from route import user
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["유저"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
