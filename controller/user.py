# user 정보, 로그인 
from db_connection import connect_db, exec_fetch_query, exec_multiple_queries, exec_query
from query import user as query
from fastapi.encoders import jsonable_encoder
from starlette.status import *
from mysql.connector import errors
from datetime import datetime, timedelta

import mysql
import jwt

def get_user():
    result = exec_fetch_query(query.SELECT_USER)

    return HTTP_200_OK, jsonable_encoder(result)

def post_user_login(user_id: str, password: str, psfa_corp: str):
    """
    로그인
    """

    query_result = exec_fetch_query(
        query.SELECT_USER_LOGIN_ID_PW,
        {
            "user_id": user_id,
            "psfa_corp": psfa_corp,
            "password": password,
        },
    )

    if not query_result:
        return HTTP_403_FORBIDDEN, {
            "code": "FAILED",
            "message": "FAILED",
        }

    query_result = jsonable_encoder(query_result)

    # JWT 발행 시각
    issued_timestamp = datetime.utcnow()

    # JWT 만료 시각
    expiration_timestamp = datetime.utcnow() + timedelta(days=1)

    token = jwt.encode(
        {
            "identity": query_result[0].get("USER_ID"),
            "iat": issued_timestamp,
            "exp": expiration_timestamp,
            "type": "access",
        },
        "eoqkrskwk",
    )

    return HTTP_200_OK, {"code": "OK", "message": "OK", "token": f"Bearer {token}"}