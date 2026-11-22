from sqlalchemy import Column, Integer, String
from app.core.database import Base
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    quantity = Column(Integer, default=0)
    # test = Column(Integer, default=0)
    # test1 = Column(Integer, default=0)

    # class config:
    #     from_attributes = True


# class Book1(Base):
#     __tablename__ = "Books1"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100), nullable=False)
#     author = Column(String(100), nullable=False)
#     quantity = Column(Integer, default=0)
#     test = Column(Integer, default=0)
#     test1 = Column(Integer, default=0)