from fastapi import APIRouter, Request, Response
from app.http.controllers.books_controller import BookController
from app.http.schemas.book_schema import BookSchema

router = APIRouter()

bc = BookController()

@router.get('/books')
def books_all(request: Request):
    return bc.show_all()

@router.post('/books')
def books_save(book: BookSchema):
    return bc.save_record(book)

@router.put('/books/{id}')
def books_update(book: BookSchema):
    return  bc.update_record(id,book)

@router.get('/books/{id}')
def books_one(id):
    return bc.show_one(id)

@router.delete('/books/{id}')
def books_delete(id):
    return bc.destroy(id)
