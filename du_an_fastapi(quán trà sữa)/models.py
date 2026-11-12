from pydantic import BaseModel, Field

class MenuItemIn(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: int = Field(gt=0)
    category: str
    
class MenuItem(MenuItemIn):
    id: int
    
class OrderLine(BaseModel):
    item_id: int
    quantity: int = Field(gt=0, le=20)
    
class OrderIn(BaseModel):
    customer_name: str = Field(min_length=1)
    lines: list[OrderLine] = Field(min_length=1)
    
class Order(OrderIn):
    id: int
    total: int
