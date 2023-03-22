from mysql.connector.errors import Error as mysqlError


# 잘못된 LOADIT USER_ID
class InvalidUserIdException(Exception):
    def __init__(self):
        self.message = "사용자를 찾을 수 없습니다."

        self.response_content = {"code": "NOT_FOUND", "message": self.message}

# 요청에 Authorization Header 포함되지 않음
class AuthHeaderNotIncludedException(Exception):
    def __init__(self):
        self.message = "인증 헤더가 포함되지 않았습니다."

        self.response_content = {"code": "NO_AUTH_HEADER", "message": self.message}
