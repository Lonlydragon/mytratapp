import sqlite3

class SQLither:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subscription (self, status = True):
        """Получаем список всех активных подписчиков в базе"""
        with self.connection:
            return self.cursor.execute("SELECT `user_name` FROM `subscription` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exist (self, user_id):
        """Проверяет есть ли юзер уже в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscription` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_name, user_id, add_date, update_date, status = True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscription` (`user_name`, `user_id`, `status`, `add_date`, `update_date`) VALUES (?,?,?,?,?)", (user_name, user_id, status, add_date, update_date))

    def update_subscription(self, user_id, status):
        """Обновляем статус подписчика"""
        return self.cursor.execute("UPDATE `subscription` SET `status` = ? WHERE user_id = ?", (status, user_id))

    def all_categories(self, user_id):
        with self.connection:
            category = []
            result = self.cursor.execute("SELECT `category_name` FROM `categories` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                category.append(row)
            category.append("Добавить новую категорию")
            return category

    def close(self):
        """Закрываем соединение с базой"""
        self.connection.close()