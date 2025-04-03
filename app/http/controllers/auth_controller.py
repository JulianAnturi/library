
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
import jose.jwt as jwt

o2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users = {
    "julian": {"username": "julian", "email": "julian@gmail.com", "password": "fakepass"}
}

class AuthController:

    SECRET_KEY = "secret_key"
    ALGORITHM = "HS256"

    def encode_token(self, payload: dict) -> str:
        token = jwt.encode(payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return token

    def decode_token(self, token: Annotated[str, Depends(o2_scheme)]) -> dict:
        try:
            data = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            user = users.get(data["username"])
            if not user:
                raise HTTPException(status_code=401, detail="Invalid token")
            return data
        except Exception as e:
            raise HTTPException(status_code=401, detail="Token decoding failed")

    def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        user = users.get(form_data.username)
        if not user or user["password"] != form_data.password:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        token = self.encode_token({"username": user["username"], "email": user["email"]})
        return {"access_token": token, "token_type": "bearer"}

    def profile(self, my_user: Annotated[dict, Depends(decode_token)]) -> dict:
        return my_user
