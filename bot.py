
import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from db import SQLither
# import exceptions
# import expenses
import categories

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

# Инициализируем соединение с БД
db = SQLither('mydatabase.db')

@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if(not db.subscriber_exist(message.from_user.id)):
        db.add_subscriber(message.from_user.first_name, message.from_user.id, message.date, message.date)
    else:
        db.update_subscription(message.from_user.id, True)
    await message.answer("Вы успешно подписаны на рассылку\nЖдите, скоро выйдут новые обзоры и вы узнаете первыми")

@dp.message_handler(commands=['unsubscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exist(message.from_user.id)):
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны")
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписались")

@dp.message_handler(commands=['get_subs'])
async def get_subscription(message: types.Message):
    await message.answer(db.get_subscription())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer(
        "Бот для учёта финансов\n\n"
        "Добавить расход: 250 такси\n"
        "Сегодняшняя статистика: /today\n"
        "За текущий месяц: /month\n"
        "Последние внесённые расходы: /expenses\n"
        "Категории трат: /categories")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
