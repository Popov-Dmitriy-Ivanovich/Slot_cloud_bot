import telebot
from telebot import types
from functions import create_items_list
from functions import create_items_table

def increase_count (object_type, object_id, increasing_rate):
    items_table = create_items_table()
    list_to_change = create_items_list(items_table, object_type)
    row_to_change = list_to_change[object_id].split(';')
    row_to_change[1] = str (int(row_to_change[1])+increasing_rate)
    list_to_change[object_id] = ";".join(row_to_change)
    rewritingfile = open(object_type+'/list.txt','w')
    for i in list_to_change:
        rewritingfile.write(i)

def show_admin_panel (bot, call, type,increasing_rate):
    items_table = create_items_table()
    list_to_show = create_items_list(items_table, type)
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(list_to_show)):
        temp_button = types.InlineKeyboardButton(list_to_show[i].split(';')[0],callback_data='change;'+type+';'+str(i)+';'+increasing_rate)
        keyboard.add(temp_button)
    bot.send_message(call.from_user.id, 'Выберите товар, количество которого вы хотели бы изменить',reply_markup=keyboard)

def admin (bot,mes):
    mes = bot.send_message(mes.from_user.id, 'вы вошли в режим изменения количества товаров\n если вы хотите изменить количество:\nкальянов - напишите hookah\n чаш - bowl\n колб - flask\n доп.услуг - extra\n для выхода из этого меню напишите cancel')
    bot.register_next_step_handler(mes, bot, admin_handler)
def admin_handler (mes, bot):
    if (mes.text == 'отмена'):
        button = types.InlineKeyboardButton('НАЖМИ МЕНЯ', callback_data = 'start')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button)
        bot.send_message(mes.from_user.id,'',reply_markup=keyboard)

        
        
