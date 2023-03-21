from pydantic import BaseModel
from typing import Union

class RegisterArgument(BaseModel):
    user_id: str
    user_pw: str
    user_nm: str

    