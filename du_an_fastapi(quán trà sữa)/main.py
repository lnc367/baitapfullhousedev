from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title = "Quán Trà Sữa Mini")
#5,6
class MenuItemIn(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: int = Field(gt=0)
    category: str

class MenuItem(MenuItemIn):
    id: int

menu = [
    {"id": 1, "name": "Trà sữa trân châu", "price": 30000, "category": "tra-sua"},
    {"id": 2, "name": "Trà đào cam sả", "price": 35000, "category": "tra-trai-cay"},
    {"id": 3, "name": "Matcha latte", "price": 40000, "category": "tra-sua"}
]
#7
def find_item(item_id: int):
    for m in menu:
        if m['id'] == item_id:
            return m
    raise HTTPException(status_code=404, detail="Không tìm thấy món")

#1
@app.get("/")
def home():
    return {"message": "Chào mừng đến với Quán Trà Sữa Mini!"}

@app.get("/about")
def about_store():
    return {
        "name": "PhucLong",
        "address": "681AuCo",
        "open": "24/7"    
    }
#2,4,7
@app.get("/menu", response_model=MenuItemIn, status_code=201)
def get_menu(max_price: int | None = None, category: str | None = None):
    result = menu
    if max_price is not None:
        result = [m for m in result if m['price'] <= max_price]
    if category is not None:
        result = [m for m in result if m["category"] == category]
    return result

@app.get("/menu/count")
def count_menu():
    return {f"total: {len(menu)}"}
#3
@app.get("/menu/{item_id}", response_model=MenuItemIn, status_code=201)
def get_item(item_id: int):
    find_item(item_id)
#5,6    
@app.post("/menu", response_model=MenuItemIn, status_code=201)
def add_item(item: MenuItemIn):
    id = max([m['id'] for m in menu], default=0) + 1
    new_item = {"id": id, **item.model_dump()}
    menu.append(new_item)
    return new_item
#7
@app.put("/menu/{item_id}", response_model=MenuItemIn)
def update_item(item_id:int, item:MenuItem):
    old = find_item(item_id)
    old.update(item.model_dump())
    return old

@app.delete("/menu/{item_id}", status_code=204)
def delete_item(item_id:int):
    menu.remove(find_item(item_id))
    return {"message": f"Bạn đã thành công xóa món {find_item(item_id)['name']}"}

#8
orders = []
class OrderItem(BaseModel):
    item_id: int
    quantity: int = Field(gt=0, le=20)

class OrderIn(BaseModel):
    customer_name: str = Field(min_length = 1)
    lines: list[OrderItem] = Field(min_length = 1)

class Order(OrderIn):
    id: int
    total: int

@app.post("/order", response_model = Order, status_code=201)
def create_order(order: OrderIn):
    total = 0
    for line in order.lines:
        item = find_item(line.item_id)
        total += item['price']
    new_order =  {"id": len(orders) + 1, "total": total, **order.model_dump()}
    orders.append(new_order)
    return new_order
