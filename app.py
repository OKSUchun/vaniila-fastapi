from db_connection import exec_query
from route import user
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["유저"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

origins = [
    "*"
    # "localhost",
    # "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)