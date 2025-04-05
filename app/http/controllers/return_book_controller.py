
# controllers/return_controller.py
from fastapi import HTTPException
from database import Database

class ReturnController:

    @staticmethod
    def return_book(user_id: int, book_id: int):
        conn = Database.get_connection()
        cursor = conn.cursor()

        # Verificar si el préstamo existe
        cursor.execute("""
            SELECT * FROM lend
            WHERE user_id = ? AND book_id = ?
        """, (user_id, book_id))
        lend = cursor.fetchone()

        if not lend:
            conn.close()
            raise HTTPException(status_code=404, detail="No hay préstamo registrado de este libro para este usuario.")

        # Obtener info del libro
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()

        if not book:
            conn.close()
            raise HTTPException(status_code=404, detail="Libro no encontrado.")

        new_quantity = book["quantity"] + 1
        new_state = 1 if book["state"] == 2 else book["state"]

        # Eliminar el préstamo
        cursor.execute("""
            DELETE FROM lend
            WHERE user_id = ? AND book_id = ?
        """, (user_id, book_id))

        # Actualizar libro
        cursor.execute("""
            UPDATE books
            SET quantity = ?, state = ?
            WHERE id = ?
        """, (new_quantity, new_state, book_id))

        conn.commit()
        conn.close()

        return {
            "message": "Libro devuelto con éxito",
            "book_id": book_id,
            "user_id": user_id,
            "nuevo_stock": new_quantity
        }
