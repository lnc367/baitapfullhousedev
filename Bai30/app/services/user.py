from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models import User
from app.schemas import sm_userread, sm_userwrite
from app.core.auth import hash_password as hp, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status

def register(db:Session, user_data:sm_userwrite):
    hashed_password = hp(user_data.hashed_password)
    user_db = User(username = user_data.username, hashed_password = hashed_password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def login(db:Session, form_data: OAuth2PasswordRequestForm):
    user_db = db.query(User).filter(User.username == form_data.username).first()
    if not user_db or not verify_password(form_data.password, user_db.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Username or Password khong chinh xac! {user_db}"
        )
    token = create_access_token({
        "user_id": str(user_db.id),
        "name": str(user_db.username)
    })
    # current_user = db.query(User).filter(and_(User.hashed_password == user.hashed_password, User.username==user.username)).first()
    return {
        "access_token": token,
        "token_type": "bearer"
    }
