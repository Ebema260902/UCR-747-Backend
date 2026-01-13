import sqlite3

def init_db():
    connection = sqlite3.connect("database.db")
    with open("scripts/init_db.sql", "r", encoding="utf-8") as file:
        sql_script = file.read()
    cursor = connection.cursor()
    cursor.executescript(sql_script)
    connection.commit()
    connection.close()
    print("Base de datos creada correctamente ✅")

if __name__ == "__main__":
    init_db()
