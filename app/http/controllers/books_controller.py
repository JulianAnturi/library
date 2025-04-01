from fastapi import Request
from fastapi.responses import JSONResponse
from app.http.controllers.controller import Controller 
from app.http.validations.book_validation import BookValidation
from app.http.schemas.book_schema import BookSchema



class BookController(Controller):
    def __init__(self, ):
        super().__init__('books',None)

    def show_all(self):
        result = self.index(self.table);
        return result

    async def save_record(self,book: BookSchema):
        data = book.model_dump()
        result = self.store(self.table,data)
        return result

    async def show_one(self, id):
        result = self.show(self.table,id )
        return result

    async def update_record(self, id, book: BookSchema):

        data = book.dict()
        result =  self.update(self.table,data, id)
        return result

    async def destroy(self, id):
        result = self.delete(self.table, id)
        return result
