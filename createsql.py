import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# # Создание таблицы
# cursor.execute("""CREATE TABLE subscription
#                   (id integer primary key autoincrement, user_name varchar(255), user_id varchar(255) NOT NULL, status BOOLEAN, add_date date, update_date date)
#                """)
# conn.commit()
#
# sql2 = "drop table `subscription`"
# cursor.execute(sql2)

# Создание таблицы
cursor.execute("""CREATE TABLE categories
                  (category_name varchar(255), user_id varchar(255) NOT NULL, add_date date)
               """)
conn.commit()

# sql2 = "drop table `categories`"
# cursor.execute(sql2)

sql = "select * from transa"
cursor.execute(sql)
print(cursor.fetchall())
#