from pydantic import BaseModel, Field
from typing import Literal

class BookSchema(BaseModel):
    name: str = Field(..., max_length=100)
    isbn: str = Field(..., max_length=20)
    url: str = Field(..., max_length=255)
    state: Literal[1, 2, 3]  # solo acepta 1, 2 o 3
    quantity: int = Field(..., ge=0)  # ge = greater or equal
    price: float = Field(..., ge=0)
    sypnosis: str = Field(..., min_length=1)

