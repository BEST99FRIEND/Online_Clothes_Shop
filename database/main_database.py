import sqlite3

DB_NAME = "stylezone_bot.db"

def create_db():
    """Bazani yaratish va kerakli jadvallarni qo‘shish"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Foydalanuvchilar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            telegram_id INTEGER UNIQUE,
            full_name TEXT,
            phone TEXT,
            language TEXT,
            gender TEXT,
            latitude REAL,
            longitude REAL
        )
    """)


    # Mahsulotlar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            image TEXT,
            quantity INTEGER DEFAULT 0
        )
    """)

    # Buyurtmalar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            product_id INTEGER,
            quantity INTEGER DEFAULT 0,
            size TEXT,
            color TEXT,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    """)

    conn.commit()
    conn.close()
