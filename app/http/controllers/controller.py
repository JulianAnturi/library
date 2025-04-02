import sqlite3 as sq

class Controller:
    def __init__(self, table=None, values=None) -> None:
        self.table = table
        self.values = values
        # Aseguramos que existe la conexión a la base de datos
        self.create_connection()

    def create_connection(self):
        # Crear las tablas si no existen
        conn = sq.connect("library.db")
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            isbn TEXT,
            url TEXT,
            state INTEGER,
            quantity INTEGER,
            price REAL,
            sypnosis TEXT
        )
        ''')
        conn.commit()
        conn.close()

    def index(self, table):
        instruction = f"SELECT * FROM {table}"
        result =  self.exec(instruction, fetch=True)
        return result

    def show(self, table, id):
        instruction = f"SELECT * FROM {table} WHERE id = ?"
        result =  self.exec(instruction, params=(id,), fetch=True)
        return result

    def store(self, table, data):
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["?" for _ in data.values()])
            values = tuple(data.values())

            instruction = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            result =  self.exec(instruction, params=values, commit=True)
            return {"success": True, "message": "Record inserted successfully"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def update(self, table, data, id):
        try:
            set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
            values = tuple(data.values()) + (id,)

            instruction = f"UPDATE {table} SET {set_clause} WHERE id = ?"
            self.exec(instruction, params=values, commit=True)
            return {"success": True, "message": "Record updated successfully"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete(self, table, id):
        instruction = f"DELETE FROM {table} WHERE id = ?"
        result =  self.exec(instruction, params=(id,), commit=True)
        return {"success": True, "message": "Record deleted successfully"}

    def exec(self, instruction, params=(), fetch=False, commit=False):
        conn = sq.connect("library.db")
        cursor = conn.cursor()

        try:
            if params:
                cursor.execute(instruction, params)
            else:
                cursor.execute(instruction)

            if commit:
                conn.commit()
                last_id = cursor.lastrowid

            if fetch:
                result = cursor.fetchall()
                return result
            elif commit:
                return last_id

        except Exception as e:
            print(f"Database error: {str(e)}")
            if commit:
                conn.rollback()
            return None
        finally:
            conn.close()
