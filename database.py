import sqlite3

def create_database():
    conn = sqlite3.connect('assets.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT,
        user TEXT,
        department TEXT,
        serial_number TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_asset(name, type, user, department, serial_number, status):
    conn = sqlite3.connect("assets.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO assets (name, type, user, department, serial_number, status) VALUES (?, ?, ?, ?, ?, ?)
    """, (name, type, user, department, serial_number, status))
    conn.commit()
    conn.close()

def get_assets():
    conn =sqlite3.connect("assets.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    assets = cursor.fetchall()
    conn.close()
    return assets

def delete_asset(asset_id):
    conn = sqlite3.connect("assets.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assets WHERE id = ?", (asset_id,))
    conn.commit()
    conn.close()

def update_asset(asset_id, name, type, user, department, serial_number, status):
    conn = sqlite3.connect("assets.db")
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE assets SET name = ?, type = ?, user = ?, department = ?, serial_number = ?, status = ? WHERE id = ?
    """, (name, type, user, department, serial_number, status, asset_id))
    conn.commit()
    conn.close()

def get_asset_by_id(asset_id):
    conn = sqlite3.connect("assets.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets WHERE id = ?", (asset_id,))
    asset = cursor.fetchone()
    conn.close()
    return asset

def get_asset_count():
    conn = sqlite3.connect("assets.db")
    cursor = conn.cursor()
    count = cursor.execute("SELECT COUNT(*) FROM assets").fetchone()[0]
    conn.close()
    return count