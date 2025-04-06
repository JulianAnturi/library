from fastapi import APIRouter, Request, Response
from app.http.controllers.books_controller import BookController
from app.http.schemas.book_schema import BookSchema



books_router = APIRouter(
    tags=["books"]
)

bc = BookController()

## Books Routes Resource
@books_router.get('/books')
def books_all(request: Request):
    return bc.show_all()

@books_router.post('/books')
def books_save(book: BookSchema):
    return bc.save_record(book)

@books_router.put('/books/{record_id}')
def books_update(record_id: int, book: BookSchema):  # ← aquí faltaba
    return bc.update_record(record_id, book)

@books_router.get('/books/{record_id}')
def books_one(record_id: int):
    return bc.show_one(record_id)

@books_router.delete('/books/{record_id}')
def books_delete(record_id:int):
    return bc.destroy(record_id)

