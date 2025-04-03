from database import Database
from fastapi import FastAPI
from routes.books_routes import books_router
from routes.auth_routes import auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(books_router)

if __name__ == '__main__':
    Database.createDB()
    Database.createTables()

