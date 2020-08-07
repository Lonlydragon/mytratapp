from aiogram import Bot, Dispatcher, executor, types

buttons = types.InlineKeyboardMarkup(row_width=2)
button0 = types.InlineKeyboardButton('Продукты', callback_data='Продукты')
button1 = types.InlineKeyboardButton('Еда', callback_data='Еда')
button2 = types.InlineKeyboardButton('Кафе', callback_data='Кафе')
button3 = types.InlineKeyboardButton('Кофе', callback_data='Кофе')
button4 = types.InlineKeyboardButton('Общ. транспорт', callback_data='Общ. транспорт')
button5 = types.InlineKeyboardButton('Такси', callback_data='Такси')
button6 = types.InlineKeyboardButton('Телефон', callback_data='Телефон')
button7 = types.InlineKeyboardButton('Интернет', callback_data='Интернет')
button8 = types.InlineKeyboardButton('Подписки', callback_data='Подписки')
button9 = types.InlineKeyboardButton('Книги', callback_data='Книги')
button10 = types.InlineKeyboardButton('Прочее', callback_data='Прочее')
buttons.add(button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)

