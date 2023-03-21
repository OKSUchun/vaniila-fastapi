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

@router.post("", description="유저 등록")
def route_post_user(user_info: RegisterArgument):
    status_code = post_user(jsonable_encoder(user_info))

    return JSONResponse(status_code=status_code, content={"status_code": status_code})

@router.post("/login", summary="로그인", description="로그인 및 토큰 발급") # TODO : 이거 구현
def route_post_login(
    request: Request,
    user_id: str = Body(...),
    password: str = Body(...),
    psfaCorp: str = Body(...),
):
    status_code, result = post_user_login(user_id, password, psfaCorp)

    return JSONResponse(status_code=status_code, content=result)

#어쩌구저쩌구 수정

