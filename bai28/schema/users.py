from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name:str = Field(...,min_length=1, max_length=100)
    email:str
    age:int | None= Field(...,gt=0, le=120)

class UserRead(BaseModel):
    id:int
    is_active:bool
    class config:
        from_attributes = True
    