import sqlite3 as sq

class Database:

    @staticmethod
    def createDB():
        conn = sq.connect('library.db')
        conn.commit()
        conn.close()

    @staticmethod
    def createTables():
        conn = sq.connect('library.db')
        cursor = conn.cursor()

        # Crear tabla users
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100),
            email TEXT UNIQUE,
            password VARCHAR(20),
            role BOOLEAN
        );
        ''')

        # Crear tabla books
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ISBN VARCHAR(20),
            name VARCHAR(100),
            url VARCHAR(255),
            state TINYINT, -- 1 disponible, 2 prestado, 3 comprado
            quantity INTEGER,
            price FLOAT,
            sypnosis TEXT
        );
        ''')

        # Crear tabla lend
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lend (
            user_id INTEGER,
            book_id INTEGER,
            date_lend DATE,
            date_deliver DATE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        );
        ''')

        # Crear tabla payments
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            user_id INTEGER,
            book_id INTEGER,
            date_payment DATE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        );
        ''')

        conn.commit()
        conn.close()

