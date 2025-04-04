from fastapi import HTTPException
from jose import jwt
from datetime import datetime, timedelta
from app.utils.auth import hash_password, verify_password
from app.http.models.user_model import User
from app.http.schemas.user_schema import UserCreate

from fastapi.responses import JSONResponse

user_model = User()

class AuthController:
    SECRET_KEY = "secret_key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    def __init__(self):
        self.user_model = User()

    def register_user(self, user_data: UserCreate):
        if self.user_model.get_user_by_email(user_data.username):
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = hash_password(user_data.password)
        user_id = self.user_model.create_user(
                name=user_data.name,
                email=user_data.username,
                password=hashed_password
                )
        data = self.login_user(user_data.username,user_data.password)
        safe_user = {user_data.name,user_data.username}
        return data


    def login_user(self, username: str, password: str):
        user = self.user_model.get_user_by_email(username)
        if not user or not verify_password(password, user["password"]):
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        payload = {
                "sub": user["email"],
                "username": user["email"],
                "role": user["role"],
                "exp": datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
                }

        safe_user = {"name":user["name"],"username": user[ "email" ], "role":user["role"]}
        token = jwt.encode(payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
        access_token =  {"access_token": token, "token_type": "bearer", "user": safe_user }

        return JSONResponse(access_token,200)


