from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.core.database import get_db
from app.models.user import User

import os
from dotenv import load_dotenv

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")
load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET", "kientkls1wsaxascsddwqeq")
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    crendentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail= "Token khong hop le",
        headers={
            "WWW-Authenticate": 'Bearer'
        }
    )

    # raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED, 
    #             detail= f"{token}-{SECRET_KEY}",
    #             headers={
    #                 "WWW-Authenticate": 'Bearer'
    #             }
    #         )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id: str = payload.get("user_id")
        if not user_id:
            raise crendentials_exc
    except:
        raise crendentials_exc

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise crendentials_exc
    return user