import telebot
from telebot import types

bot = telebot.TeleBot('7355946689:AAHoySPBqU7VA9cnX6thgqATL1dhgTcm-t0')

@bot.message_handler(commands=['start'])
def start(message):
    markup1= types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('Забронировать столик', callback_data='bron'))
    user_name = message.from_user.username
    bot.send_message(message.chat.id, f'Привет, @{user_name}, нажми кнопку, для того чтобы забронировать столик', reply_markup=markup1)
    
    
bot.polling(none_stop=True)


