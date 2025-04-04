from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: EmailStr
    name: str
    role: bool

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str 
    role: bool 

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserBase  # si solo quieres mostrar el nombre y username
