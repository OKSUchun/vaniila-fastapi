from db_connection import connect_db, exec_fetch_query, exec_multiple_queries, exec_query
from query import user as query
from fastapi.encoders import jsonable_encoder
from starlette.status import *
from mysql.connector import errors

import mysql

def get_user():
    result = exec_fetch_query(query.SELECT_USER)

    return HTTP_200_OK, jsonable_encoder(result)
