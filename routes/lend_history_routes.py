
# routers/lend_history.py
from fastapi import APIRouter
from app.http.controllers.lend_history_controller import LendHistoryController

lend_history_router = APIRouter(prefix="/lend/history", tags=["lend history"])

@lend_history_router.get("/{user_id}")
def get_history(user_id: int):
    return LendHistoryController.get_user_lend_history(user_id)
