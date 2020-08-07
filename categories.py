import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

def all_categories():
    sql = "select name from categories"
    cursor.execute(sql)
    choise = []
    for row in cursor.execute(sql):
        choise.append(row)
    print(choise)
