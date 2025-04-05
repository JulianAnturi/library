from pydantic import BaseModel, EmailStr, Field

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



class UserSchema(BaseModel):
    name: str = Field(..., max_length=100)
    username: str = Field(..., max_length=20)
    role: bool = Field(..., max_length=255)
    email: str = Field(..., ge=0)  # ge = greater or equal
    password: float = Field(..., ge=0)
    sypnosis: str = Field(..., min_length=1)
