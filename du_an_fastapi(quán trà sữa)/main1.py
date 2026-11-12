from fastapi import FastAPI
from routers import menu, orders

app = FastAPI(title="Quán Trà Sữa Mini")

app.include_router(menu.router)
app.include_router(orders.router)

@app.get("/")
def home():
    return {"message": "Chào mừng đến Quán Trà Sữa Mini!"}