# routers/lend.py
from fastapi import APIRouter
from app.http.controllers.lend_controller import LendController
from app.http.schemas.lend_schema import LendCreate

lend_router = APIRouter(prefix="/lend", tags=["lends"])

@lend_router.post("/")
def prestar_libro(lend_data: LendCreate):
    return LendController.lend_book(lend_data)
