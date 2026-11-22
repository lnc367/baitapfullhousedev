from fastapi import FastAPI
from .core.database import Base, engine
from .routers import book_router, user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quản lý thư viện cá nhân")

app.include_router(book_router)
app.include_router(user_router)

@app.get("/")
def welcome():
    return {
        "Message": "Chào mừng bạn đến với ứng dụng quản lý thư viện cá nhân của mình"
    }


