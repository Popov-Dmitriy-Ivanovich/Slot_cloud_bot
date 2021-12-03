import telebot
from telebot import types
from config import TYPE
from functions import create_items_list
from functions import create_items_table
def show_item_list (bot,chat_id,title,item_list): #sends message to user, including all options from item_list (array of options)
    keyboard = types.InlineKeyboardMarkup()
    callback_button_back = types.InlineKeyboardButton('<- назад', callback_data = 'catalog')
    for i in item_list:
        temparr = i.split(';')
        if int(temparr[1]) > 0:
            callback_button_temp = types.InlineKeyboardButton(temparr[0],callback_data='info'+temparr[2]+';'+temparr[3][:-1])
            keyboard.add(callback_button_temp)
    keyboard.add(callback_button_back)
    bot.send_message(chat_id,title,reply_markup= keyboard)
    

def show_catalog (bot, call): 
    items_table = create_items_table()
    callback_button_hookah = types.InlineKeyboardButton('Кальяны',callback_data = 'show_hookah')
    callback_button_bowl = types.InlineKeyboardButton('Чаши',callback_data = 'show_bowl')
    callback_button_flask = types.InlineKeyboardButton('Колбы',callback_data = 'show_flask')
    callback_button_tobacco = types.InlineKeyboardButton('Табак',callback_data = 'show_tobacco')
    callback_button_extra = types.InlineKeyboardButton('Дополнительные услуги',callback_data = 'show_extra') 
    callback_button_back = types.InlineKeyboardButton('<- назад',callback_data = 'start')
    keyboard = types.InlineKeyboardMarkup();
    keyboard.add(callback_button_hookah)
    keyboard.add(callback_button_bowl)
    keyboard.add(callback_button_flask)
    keyboard.add(callback_button_tobacco)
    keyboard.add(callback_button_extra)
    keyboard.add(callback_button_back)
    bot.send_message(call.message.chat.id,'Каталог:',reply_markup=keyboard)
    bot.delete_message(call.message.chat.id, call.message.id)