import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токен вашего бота
bot_token = '6346820494:AAFUDgnUU8cCe4oAYH4kOdGeK5GrBl_qyCU'

# Создаем объект бота
bot = telebot.TeleBot(bot_token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = """
Привет, друг!
Это бот, который сделает тебя частью крипто-движухи! Тут ты можешь:

💳 Купить криптовалюту прямиком с карты! Быстро, удобно и без лишней возни.

🔄 Обменять валюту? Легко! Переключай свои ассеты так, как ты хочешь, когда хочешь.

🔐 Открыть крипто-кошелек — твой персональный хранилище для цифрового золота!

🎰 Розыгрыш? Да! Вовлекай свою удачу и побеждай в захватывающих викторинах на крипту.

💎 И держись крепче... Стейкинг TON! Получай пассивный доход, стань частью комьюнити TON и дай своим токенам работать на тебя.

Я жду: дай мне знать, и я тебе во всём помогу.
"""

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Купить с карты", url='http://t.me/CryptoBot'))
    keyboard.add(InlineKeyboardButton("Обменять крипту", url='http://t.me/CryptoBot'))  # Assuming there's an exchange bot
    keyboard.add(InlineKeyboardButton("Открыть кошелек", url='http://t.me/CryptoBot'))  # Assuming there's a wallet bot
    keyboard.add(InlineKeyboardButton("Розыгрыш", url='http://t.me/TONStartBot'))
    keyboard.add(InlineKeyboardButton("Стейкинг TON", url='http://t.me/StakeeBot'))

    bot.send_message(message.chat.id, welcome_message, reply_markup=keyboard, parse_mode='HTML')

# Запускаем бота
bot.polling()