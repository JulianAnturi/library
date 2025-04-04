from database import Database
from typing import Optional

class User:
    def create_user(self,name: str, email: str, password: str, role: bool = False):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
                (name, email, password, role)
            )
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def get_user_by_email(self,email: str) -> Optional[dict]:
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return dict(row)
        return None

