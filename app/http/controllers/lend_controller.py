# controllers/lend_controller.py
from datetime import date
from fastapi import HTTPException
from database import Database
from app.http.schemas.lend_schema import LendCreate

class LendController:

    @staticmethod
    def lend_book(lend_data: LendCreate):
        conn = Database.get_connection()
        cursor = conn.cursor()

        # Verificar que el libro existe
        cursor.execute("SELECT * FROM books WHERE id = ?", (lend_data.book_id,))
        book = cursor.fetchone()

        if not book:
            raise HTTPException(status_code=404, detail="Libro no encontrado")

        # Verificar disponibilidad
        # return book["state"]
        if book["state"] == 0 or book["quantity"] <= 0:
            raise HTTPException(status_code=400, detail="Libro no disponible para préstamo")

        # Insertar préstamo
        cursor.execute('''
            INSERT INTO lend (user_id, book_id, date_lend, date_deliver)
            VALUES (?, ?, ?, ?)
        ''', (
            lend_data.user_id,
            lend_data.book_id,
            lend_data.date_lend.isoformat(),
            lend_data.date_deliver.isoformat()
        ))

        # Actualizar cantidad y estado del libro
        new_quantity = book["quantity"] - 1
        new_state = 2 if new_quantity == 0 else 1

        cursor.execute('''
            UPDATE books SET quantity = ?, state = ? WHERE id = ?
        ''', (new_quantity, new_state, lend_data.book_id))

        conn.commit()
        conn.close()

        return {
            "message": "Préstamo registrado exitosamente",
            "user_id": lend_data.user_id,
            "book_id": lend_data.book_id,
            "date_lend": lend_data.date_lend,
            "date_deliver": lend_data.date_deliver
        }

