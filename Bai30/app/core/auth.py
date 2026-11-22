import bcrypt 
from datetime import datetime, timedelta, timezone
from jose import jwt
import os
from dotenv import load_dotenv
# from fastapi import HTTPException, status

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET", "kientkls1wsaxascsddwqeq")
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password:str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain:str, hashed:str) -> bool:
    # raise HTTPException(status_code=200, detail={
    #     "plain":plain,
    #     "hashed":hashed
    # })
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))

def create_access_token(data:dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp": expire
    })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)







