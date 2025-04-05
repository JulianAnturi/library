# controllers/lend_history_controller.py
from database import Database
from datetime import datetime

class LendHistoryController:

    @staticmethod
    def get_user_lend_history(user_id: int):
        conn = Database.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT 
                l.user_id, 
                l.book_id, 
                l.date_lend, 
                l.date_deliver, 
                b.name AS book_name
            FROM lend l
            JOIN books b ON l.book_id = b.id
            WHERE l.user_id = ?
            ORDER BY l.date_lend DESC
        ''', (user_id,))

        rows = cursor.fetchall()
        conn.close()

        today = datetime.now().date()
        history = []

        for row in rows:
            row_dict = dict(row)
            deliver_date = datetime.strptime(row["date_deliver"], "%Y-%m-%d").date()
            row_dict["status"] = "En curso" if deliver_date >= today else "Devuelto"
            history.append(row_dict)

        return history
