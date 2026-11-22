from pydantic import BaseModel, Field

class BookWrite(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    quantity: int = Field(default=0)

class BookRead(BookWrite):
    id: int
    class config:
        from_attributes = True