from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from app.http.controllers.auth_controller import AuthController
from app.http.schemas.user_schema import UserCreate, Token

auth_router = APIRouter(
        tags=["Authentication"]
        )
auth_controller = AuthController()

@auth_router.post("/register")
def register(user_data: UserCreate):
    return auth_controller.register_user(user_data)

@auth_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth_controller.login_user(form_data.username, form_data.password)
