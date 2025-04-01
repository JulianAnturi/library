from database import Database
from fastapi import FastAPI
from routes.api import router

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    Database.createDB()
    Database.createTables()


