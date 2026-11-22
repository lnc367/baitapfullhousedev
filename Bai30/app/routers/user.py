from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from ..core.database import get_db
from sqlalchemy.orm import Session
from ..services import user_register, user_login
from ..schemas import sm_userwrite, sm_userread
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/users", tags = ['Users'])

@router.post("/register", response_model=sm_userread)
def register(user:sm_userwrite, db:Session = Depends(get_db)):
    user_db = user_register(db, user)
    return user_db

@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends(), db:Session= Depends(get_db)):
    current_user = user_login(db, form_data)
    return current_user