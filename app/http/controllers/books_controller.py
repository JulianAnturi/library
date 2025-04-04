from fastapi import Request
from fastapi.responses import JSONResponse
from app.http.controllers.controller import Controller 
from app.http.schemas.book_schema import BookSchema



class BookController(Controller):
    def __init__(self, ):
        super().__init__('books',None)

    def show_all(self):
        try:
            result =  self.index(self.table);
            return JSONResponse(result,200)
        except Exception:
            raise Exception("ups, something went wrong")


    def save_record(self,book: BookSchema):
        try:
            data = book.model_dump()
            result = self.store(self.table,data)
            return JSONResponse(result, 200)
        except Exception:
            raise Exception("ups, something went wrong")

    def show_one(self, id):
        try:
            result = self.show(self.table,id )
            return JSONResponse(result, 200)
        except Exception:
            raise Exception("ups, something went wrong")

    def update_record(self, id, book: BookSchema):
        try:
            data = book.model_dump()
            result =   self.update(self.table,data, id)
            return result

        except Exception:
            raise Exception("ups, something went wrong")

    def destroy(self, id):
        try:
            result = self.delete(self.table, id)
            return result
        except Exception:
            raise Exception("ups, something went wrong")

