SELECT_USER = """
SELECT `USER_ID`
     , `USER_PW`
     , `USER_NM`
  FROM USERS.USER
"""
SELECT_USER_LOGIN_ID_PW = """
SELECT * 
  FROM USERS.USER
 WHERE USER_ID = %(user_id)s
   AND PSFA_CORP = %(psfa_corp)s
   AND PASSWORD = %(password)s
;
"""