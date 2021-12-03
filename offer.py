from telebot import types
from config import *
from functions import *
from functions import cancel_button

def show_offer_options_hookah (bot, call):
    hookah_list = create_items_list(create_items_table(), 'hookah')
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(hookah_list)):
        if (int(hookah_list[i].split(';')[1])>0):
            callback_button_temporary = types.InlineKeyboardButton(hookah_list[i].split(';')[0],callback_data = 'offer_step2;'+str(i))
            keyboard.add(callback_button_temporary)
    keyboard.add(cancel_button)
    bot.send_message(call.from_user.id, 'Выберете кальян, который вы хотели бы заказать:', reply_markup=keyboard)

def show_offer_options_flask (bot, call):
    flask_list = create_items_list(create_items_table(), 'flask')
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(flask_list)):
        if (int(flask_list[i].split(';')[1])>0):
            callback_button_temporary = types.InlineKeyboardButton(flask_list[i].split(';')[0],callback_data = 'offer_step3;'+str(i))
            keyboard.add(callback_button_temporary)
    keyboard.add(cancel_button)
    bot.send_message(call.from_user.id, 'Выберете колбу, которую вы хотели бы заказать:', reply_markup=keyboard)

def show_offer_options_bowl (bot, call):
    flask_list = create_items_list(create_items_table(), 'bowl')
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(flask_list)):
        if (int(flask_list[i].split(';')[1])>0):
            callback_button_temporary = types.InlineKeyboardButton(flask_list[i].split(';')[0],callback_data = 'offer_step4;'+str(i))
            keyboard.add(callback_button_temporary)
    keyboard.add(cancel_button)
    bot.send_message(call.from_user.id, 'Выберете чашу, которую вы хотели бы заказать:', reply_markup=keyboard)

