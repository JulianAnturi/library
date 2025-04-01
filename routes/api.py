from fastapi import APIRouter, Request, Response
from app.http.controllers.books_controller import BookController
from app.http.schemas.book_schema import BookSchema

router = APIRouter()

bc = BookController()

@router.get('/books')
def books_all(request: Request):
    return bc.show_all()

@router.post('/books')
async def books_save(book: BookSchema):
    return await bc.save_record(book)

@router.put('/books/{id}')
def books_update(book: BookSchema):
    return  bc.update_record(id,book)
