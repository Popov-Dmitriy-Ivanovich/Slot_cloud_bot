from config import TOKEN
from config import ADMIN_ID
from catalog import *
import telebot
from telebot import types
import offer
from functions import cancel_button
import admin
OFFER_DATA = dict()
bot = telebot.TeleBot(TOKEN)
bot.send_message(ADMIN_ID, "Slot_cloud bot is working")
@bot.message_handler(func= lambda m: m.text == '/id')
def send_id (message):
    bot.send_message(message.from_user.id, message.from_user.id)

@bot.message_handler(func= lambda m: m.text == '/user_name')
def send_id (message):
    bot.send_message(message.from_user.id, message.from_user.username)

@bot.message_handler(func = lambda m: m.text == '/delete')
def clear (message):
        bot.delete_message(message.chat.id, message.message_id-1)

@bot.message_handler(func = lambda m: m.text == '/admin')
def admin_boot (mes):
    if(mes.from_user.id == ADMIN_ID):
        ask = bot.send_message(mes.from_user.id,'насколько вы хотели бы увеличить количество товара? (отправьте боту сообщение, отрицательное чилсо уменьшит количество товара)')
        bot.register_next_step_handler(ask, change_handler)
   

def change_handler (mes):
    callback_button_change_hookah = types.InlineKeyboardButton('Кальяны', callback_data = 'choice:hookah:' + mes.text)    
    callback_button_change_bowl = types.InlineKeyboardButton('Чаши',callback_data = 'choice:bowl:' + mes.text)
    callback_button_change_flask = types.InlineKeyboardButton('Калбы',callback_data = 'choice:flask:' + mes.text)
    callback_button_change_extra = types.InlineKeyboardButton('Доп услуги',callback_data = 'choice:extra:' + mes.text)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_change_bowl)
    keyboard.add(callback_button_change_hookah)
    keyboard.add(callback_button_change_flask)
    keyboard.add(callback_button_change_extra)
    bot.send_message(mes.from_user.id, 'выберите категорию товара, количество товара в которой вы хотели бы изменить', reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: call.data[:6]=='choice')
def choice_process (call):
    admin.show_admin_panel(bot,call, call.data.split(':')[1],call.data.split(':')[2])

@bot.callback_query_handler(func = lambda call: call.data[:6] == 'change')
def process_change (call):
    admin.increase_count(call.data.split(';')[1], int(call.data.split(';')[2]), int (call.data.split(';')[3]))
    bot.send_message(call.from_user.id, 'Изменение количества прошло успешно!')
@bot.message_handler(func = lambda m: m.text == '/start')
def start_message (message):    
    keyboard = types.InlineKeyboardMarkup()
    callback_button_catalog = types.InlineKeyboardButton(text="Посмотреть каталог", callback_data="catalog")
    callback_button_offer = types.InlineKeyboardButton(text="сделать заказ", callback_data="offer")
    callback_button_info = types.InlineKeyboardButton( text = 'О нас', callback_data = 'info')
    callback_button_rules = types.InlineKeyboardButton(text= 'правила', callback_data = 'rules')
    keyboard.add(callback_button_catalog,callback_button_offer)
    keyboard.add(callback_button_info,callback_button_rules)
    bot.send_message(message.from_user.id, 'Вас приветствует бот Slot_cloud, скажите, что вы хотите сделать:', reply_markup= keyboard)
    bot.delete_message(message.from_user.id, message.id)

@bot.callback_query_handler(func=lambda call: call.data == "start") #show catalog
def test_callback(call): # <- passes a CallbackQuery type object to your function
    keyboard = types.InlineKeyboardMarkup()
    callback_button_catalog = types.InlineKeyboardButton(text="Посмотреть каталог", callback_data="catalog")
    callback_button_offer = types.InlineKeyboardButton(text="сделать заказ", callback_data="offer")
    keyboard.add(callback_button_catalog,callback_button_offer)
    callback_button_info = types.InlineKeyboardButton( text = 'О нас', callback_data = 'info')
    callback_button_rules = types.InlineKeyboardButton(text= 'правила', callback_data = 'rules')
    keyboard.add(callback_button_info,callback_button_rules)
    bot.send_message(call.from_user.id, 'Вас приветствует бот Slot_cloud, скажите, что вы хотите сделать:', reply_markup= keyboard)
    bot.delete_message(call.message.chat.id,call.message.id)
@bot.callback_query_handler(func = lambda call:call.data == 'info')
def show_info (call):
    callback_button_menu = types.InlineKeyboardButton('меню', callback_data = 'start')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_menu)
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.from_user.id,'Дата создания: 19.11.2021 \n\nПримерное время ожидания подтверждения заказа: 10 минут (за частую отвечаем в течении минуты!)\n\nСамовывоз работает с 8:00 до 23:00\nДоставка работает с 18:00 до 23:00\n\nДоставка кальяна на дом:\nЛенинский район: до 40 минут\nОктябрьский район: до 30 минут\nСоветский район: до 50 минут\nСтроитель: до 1 часа 20 минут\n\nКонтакты поддержки:\ninst: @slot_sergey\nwats app: +79806773421\ntg: @slotsalat\nМобильный телефон (может быть недоступен. В таком случае звонки принимаются в wats app): +79806773421',reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: call.data == 'rules')
def show_rules(call):
    callback_button_menu = types.InlineKeyboardButton('меню', callback_data = 'start')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_menu) 
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_document(call.from_user.id, open('Dogovor_Arendy.docx','rb'),caption='Наши правила очень просты:\n1. Корректное оформление заказа😃\n2. Всегда быть на связи📲\n3. Соблюдать условия договора (он будет прикреплён ниже для ознакомления)📃\n4. Получать массу удовольствия от пользования нашими услугами😊', reply_markup = keyboard)   
@bot.callback_query_handler(func=lambda call: call.data == "catalog") #show catalog
def test_callback(call): # <- passes a CallbackQuery type object to your function
    show_catalog(bot, call)

@bot.callback_query_handler( func = lambda call: call.data == 'show_hookah')
def answer_callback (call):
    show_item_list(bot, call.from_user.id, 'Список кальянов в наличии:', create_items_list (create_items_table(),'hookah'))
    bot.delete_message(call.message.chat.id, call.message.id)

@bot.callback_query_handler( func = lambda call: call.data == 'show_bowl')
def answer_callback (call):
    show_item_list(bot, call.from_user.id, 'Список чаш в наличии:', create_items_list (create_items_table(),'bowl'))
    bot.delete_message(call.message.chat.id, call.message.id)

@bot.callback_query_handler( func = lambda call: call.data == 'show_flask')
def answer_callback (call):
    show_item_list(bot, call.from_user.id, 'Список колб в наличии:', create_items_list (create_items_table(),'flask'))
    bot.delete_message(call.message.chat.id, call.message.id)

@bot.callback_query_handler( func = lambda call: call.data == 'show_tobacco')
def answer_callback (call):
    show_item_list(bot, call.from_user.id, 'Список табака в наличии:', create_items_list (create_items_table(),'tobacco'))
    bot.delete_message(call.message.chat.id, call.message.id)

@bot.callback_query_handler( func = lambda call: call.data == 'show_extra')
def answer_callback (call):
    show_item_list(bot, call.from_user.id, 'Список дополнительных услуг:', create_items_list (create_items_table(),'extra'))
    bot.delete_message(call.message.chat.id, call.message.id)

@bot.callback_query_handler(func = lambda call: call.data[0:4] == 'info')
def answer_callback (call):
    text_file = open (call.data[4:].split(';')[0])
    path = call.data[4:].split(';')[1]
    photo = open(path, 'rb')
    callback_button_hideinfo = types.InlineKeyboardButton('<-назад', callback_data='hide_info')
    keyboardmarkup = types.InlineKeyboardMarkup()
    keyboardmarkup.add(callback_button_hideinfo)
    bot.send_photo(call.from_user.id, photo, caption=text_file.read(),reply_markup=keyboardmarkup)
    #bot.send_message(call.from_user.id,path)
@bot.callback_query_handler(func = lambda call: call.data == 'hide_info')
def answer_callback (call):
    bot.delete_message(call.message.chat.id,call.message.id)

@bot.callback_query_handler(func=lambda call: call.data == "offer") #show offer
def offer_making(call): 
    bot.delete_message(call.message.chat.id, call.message.id)
    ask = bot.send_message(call.from_user.id, 'Чтобы присупить к оформлению заказа укажите номер вашего телефона') 
    bot.register_next_step_handler(ask, get_number)
def get_number(mes):
    callback_button_next = types.InlineKeyboardButton('далее',callback_data = 'offer_step1')
    callback_button_cancel = types.InlineKeyboardButton('отмена',callback_data = 'start')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_next)
    keyboard.add(callback_button_cancel)
    OFFER_DATA [mes.from_user.id] = mes.text
    bot.delete_message(mes.chat.id,mes.id)
    bot.delete_message(mes.chat.id,mes.id-1)
    bot.send_message(mes.from_user.id,'Ваш номер: '+OFFER_DATA[mes.from_user.id],reply_markup=keyboard)
    
@bot.callback_query_handler(func = lambda call: call.data == 'offer_step1')
def offer_step1_function (call):
    bot.delete_message(call.message.chat.id,call.message.id)
    offer.show_offer_options_hookah(bot, call)

@bot.callback_query_handler(func = lambda call: call.data[:11]=='offer_step2')
def offer_step2_handl (call):
    OFFER_DATA[call.from_user.id] +='\n' + str(create_items_list(create_items_table(), 'hookah')[int(call.data[12:])].split(';')[0])
    bot.delete_message(call.message.chat.id,call.message.id)
    offer.show_offer_options_flask(bot, call)

@bot.callback_query_handler(func = lambda call: call.data[:11]=='offer_step3')
def offer_step3_handl (call):
    OFFER_DATA[call.from_user.id] +='\n' + str(create_items_list(create_items_table(), 'flask')[int(call.data[12:])].split(';')[0])
    bot.delete_message(call.message.chat.id,call.message.id)
    offer.show_offer_options_bowl(bot, call)
@bot.callback_query_handler (func = lambda call: call.data[:11]=='offer_step4')
def offer_step4_handl (call):
    OFFER_DATA[call.from_user.id] +='\n' + str(create_items_list(create_items_table(), 'bowl')[int(call.data[12:])].split(';')[0])
    callback_button_withTobacco = types.InlineKeyboardButton('да', callback_data = 'offer_step5;y')
    callback_button_withNOTobacco = types.InlineKeyboardButton('нет', callback_data = 'offer_step5;n')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_withNOTobacco,callback_button_withTobacco)
    keyboard.add(cancel_button)
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.from_user.id, 'Вы будете арендовать кальян с табаком?', reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: call.data[:11] == 'offer_step5')
def offer_step5_handl (call):
    print('worked')
    if call.data[-1] == 'n':
        OFFER_DATA[call.from_user.id]+='\n'+'Без табака'
    else:
        OFFER_DATA[call.from_user.id]+='\n'+'С табаком'
    callback_button_withShipping = types.InlineKeyboardButton('Доставка', callback_data = 'offer_step6;1')
    callback_button_withNOShipping = types.InlineKeyboardButton('Самовывоз', callback_data = 'offer_step6;0')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_withNOShipping)
    keyboard.add(callback_button_withShipping)
    keyboard.add(cancel_button)
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.from_user.id, 'Выберете способ доставки кальяна', reply_markup = keyboard)       

@bot.callback_query_handler(func = lambda call: call.data[:11] == 'offer_step6')
def offer_step5_handl (call):
    #print('worked')
    if call.data[-1] == '1':
        OFFER_DATA[call.from_user.id]+='\n'+'Доставка'
    else:
        OFFER_DATA[call.from_user.id]+='\n'+'Самовывоз'
    callback_button_card = types.InlineKeyboardButton('Переводом на банковскую карту (Сбер, Тинькофф)', callback_data = 'offer_step7;T')
    callback_button_money = types.InlineKeyboardButton('Наличными', callback_data = 'offer_step7;M')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_card)
    keyboard.add(callback_button_money)
    keyboard.add(cancel_button)
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.from_user.id, 'Выберете способ оплаты', reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: call.data[:11]=='offer_step7')
def offer_step7_handl (call):
    if call.data[-1] == 'T':
        OFFER_DATA[call.from_user.id]+='\n'+'оплата картой (перевод на сбер/тинькофф'
    else:
        OFFER_DATA[call.from_user.id]+='\n'+'оплата наличными'
    callback_button_confirm = types.InlineKeyboardButton('подтвердить', callback_data = 'confirm')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_confirm)
    keyboard.add(cancel_button)
    bot.delete_message(call.message.chat.id,call.message.id)
    bot.send_message(call.from_user.id, 'Подтверидте заказ', reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: call.data[:11]=='confirm')
def offer_step7_handl (call):
    callback_button_confirm = types.InlineKeyboardButton('готово', callback_data = 'start')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_confirm)
    bot.delete_message(call.message.chat.id,call.message.id)
    bot.send_message(ADMIN_ID, OFFER_DATA[call.from_user.id])
    OFFER_DATA.pop(call.from_user.id)
    bot.send_message(call.from_user.id, 'ваш заказ подтверждён, в ближайшее время с вами свяжется наш сотрудник', reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: call.data == 'cancel')
def cancel_handl(call):
    bot.delete_message(call.message.chat.id,call.message.id)
    OFFER_DATA.pop(call.from_user.id)
    callback_button_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data = 'start')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(callback_button_menu)
    bot.send_message(call.from_user.id, 'ваш заказ отменён',reply_markup=keyboard)
bot.polling();