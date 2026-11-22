from pydantic import BaseModel, Field

class UserWrite(BaseModel):
    username: str = Field(..., min_length=1, max_length=100)
    hashed_password: str = Field(..., min_length=1, max_length=100)

class UserRead(BaseModel):
    id: int
    username: str = Field(..., min_length=1, max_length=100)
    class config:
        from_attributes = True