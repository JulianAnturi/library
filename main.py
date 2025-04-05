from database import Database
import uvicorn
import os
from fastapi import FastAPI
from routes.books_routes import books_router
from routes.users_routes import users_router
from routes.auth_routes import auth_router
from routes.lend_routes import lend_router
from routes.return_book_routes import return_book_router
from routes.lend_history_routes import lend_history_router


app = FastAPI()

# app.include_router(router)

app.include_router(return_book_router)
app.include_router(auth_router)
app.include_router(books_router)
app.include_router(users_router)
app.include_router(lend_router)

app.include_router(lend_history_router)
if __name__ == '__main__':
    Database.createDB()
    Database.createTables()


@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde tu biblioteca favorita!"}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Render define este valor automáticamente
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
