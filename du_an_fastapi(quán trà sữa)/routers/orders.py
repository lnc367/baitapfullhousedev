from fastapi import APIRouter

from database import load_data, save_data
from models import Order, OrderIn
from routers.menu import find_item

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("", response_model=Order, status_code=201)
def create_order(order: OrderIn):
    data = load_data()
    total = 0
    for line in order.lines:
        total += find_item(data["menu"], line.item_id)["price"] * line.quantity
    new_order = {"id": len(data["orders"]) + 1, "total": total, **order.model_dump()}
    data["orders"].append(new_order)
    save_data(data)
    return new_order

@router.get("", response_model=list[Order])
def get_orders():
    return load_data()["orders"]