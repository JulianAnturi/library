from pydantic import BaseModel
from datetime import date

class LendBase(BaseModel):
    user_id: int
    book_id: int
    date_lend: date
    date_deliver: date

class LendCreate(LendBase):
    pass  # Igual que el base, pero puedes extender en el futuro

class Lend(LendBase):
    class Config:
        orm_mode = True
