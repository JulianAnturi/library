
# routers/return.py
from fastapi import APIRouter
from app.http.controllers.return_book_controller import ReturnController

return_book_router = APIRouter(prefix="/return", tags=["return books"])

@return_book_router.post("/{user_id}/{book_id}")
def return_book(user_id: int, book_id: int):
    return ReturnController.return_book(user_id, book_id)
