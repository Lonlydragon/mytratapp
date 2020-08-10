
import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from db import SQLither
import categories
import keyboard

# import exceptions
# import expenses


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

@dp.message_handler(commands=['add_categories'])
async def add_categories(message: types.Message):
    await message.answer(db.all_categories(message.from_user.id))
    buttons = types.InlineKeyboardMarkup()
    buttons.add(db.all_categories(message.from_user.id))
    await message.answer('Категории', reply_markup=buttons)

@dp.message_handler()
async def add_trans(message: types.Message):
    await message.answer(text=message.text, reply_markup=keyboard.buttons)
    await message.delete()

@dp.callback_query_handler()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id, text=callback_query.message.text + ' ' + callback_query.data, show_alert=True)
    if callback_query.data != 'category_change':
        await bot.edit_message_text(message_id=callback_query.message.message_id, chat_id=callback_query.from_user.id,
                                text=callback_query.message.text + ' ' +callback_query.data,
                                reply_markup=keyboard.retry)
    else:
        await bot.answer_callback_query(callback_query.id, show_alert=True, text='пока нечего')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
