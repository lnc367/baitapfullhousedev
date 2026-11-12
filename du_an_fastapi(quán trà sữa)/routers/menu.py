from fastapi import APIRouter, HTTPException

from models import MenuItemIn, MenuItem
from database import load_data, save_data

router = APIRouter(prefix="/menu", tags=["Menu"])

def find_item(menu, item_id: int):
    for m in menu:
        if m['id'] == item_id:
            return m
    raise HTTPException(status_code=404, detail="Không tìm thấy món")

@router.get("", response_model=list[MenuItem])
def get_menu(max_price: int | None = None, category: str | None = None):
    result = load_data()["menu"]
    if max_price is not None:
        result = [m for m in result if m['price'] <= max_price]
    if category is not None:
        result = [m for m in result if m["category"] == category]
    return result

@router.get("/{item_id}", response_model=MenuItem)
def get_item(item_id: int):
    return find_item(load_data()["menu"], item_id)

@router.post("", response_model=MenuItem, status_code=201)
def add_item(item: MenuItemIn):
    data = load_data()
    new_id = max([m["id"] for m in data["menu"]], default=0) + 1
    new_item = {"id": new_id, **item.model_dump()}
    data["menu"].append(new_item)
    save_data(data)
    return new_item

@router.put("/{item_id}", response_model=MenuItem)
def update_item(item_id: int, item: MenuItemIn):
    data = load_data()
    old = find_item(data["menu"], item_id)
    old.update(item.model_dump())
    save_data(data)
    return old

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    data = load_data()
    data["menu"].remove(find_item(data["menu"], item_id))
    save_data(data)