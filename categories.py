import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

result = cursor.execute("SELECT category_name FROM `categories`").fetchall()
print(result)

new = []

for row in result:
    new.append(row[-1])