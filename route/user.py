from fastapi import APIRouter, Body, Request, Header, Query
from fastapi.responses import JSONResponse
from controller.user import *

router = APIRouter()

@router.get("/", description="유저 정보조회")
def route_get_user():
    status_code, result = get_user()

    return JSONResponse(
        status_code=status_code,
        content=result,
    )
