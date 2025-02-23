import telebot
from telebot import types

# Замените 'YOUR_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7854686343:AAETb0ziaeq4x3od9VFkD_B_YKOF_24QP4c')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Открыть веб-приложение", web_app=types.WebAppInfo(url="https://ipojn.github.io/tgbot.github.io/"))
    keyboard.add(button)

    bot.send_message(message.chat.id, "Привет! Нажми на кнопку ниже, чтобы открыть веб-приложение:", reply_markup=keyboard)

# Запуск бота
bot.polling()
