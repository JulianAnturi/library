
# models/lend.py
from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

class Lend():
    __tablename__ = "lend"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    date_lend = Column(Date)
    date_deliver = Column(Date)

    user = relationship("User")
    book = relationship("Book")
