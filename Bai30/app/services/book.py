
from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import sm_bookread, sm_bookwrite

def get_books(db:Session):
    return db.query(Book).all()

def get_book(db:Session, book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db:Session, book_data:sm_bookwrite):
    book = Book(**book_data.model_dump())
    try:
        db.add(book)
        db.commit()
        db.refresh(book)
        return book
    except:
        db.rollback()
        return None