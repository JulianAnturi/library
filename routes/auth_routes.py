
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.http.controllers.auth_controller import AuthController

auth_router = APIRouter(
        tags=["auth"]
        )

auth_controller = AuthController()

@auth_router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return auth_controller.login(form_data)

@auth_router.get("/profile")
def get_profile(my_user: Annotated[dict, Depends(auth_controller.decode_token)]):
    return auth_controller.profile(my_user)
