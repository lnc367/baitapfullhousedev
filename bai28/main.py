from database import Base, engine
from models import User
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from services import get_user, create_user as cu
from schema import UserRead, UserCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/home")
def home():
    return{
        "message":"home"
    }

# @app.post("/users")
# def create_user(user: UserCreate,db:Session=Depends(get_db)):
#     return cu(db=db, user=user)