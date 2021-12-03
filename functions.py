from config import *
from telebot import types
cancel_button = types.InlineKeyboardButton('Отмена заказа',callback_data='cancel')
def create_items_table ():  #loads data from files, returns list of lists, first element of every list is groupname
    output = []
    
    for i in TYPE:
        temp =[]
        temp.append(i)
        input_file = open(i+'/list.txt')
        for line in input_file:
            temp.append(line)
        output.append(temp)
    return output

def create_items_list (input_table, key): #returns list of all items in group (like all hookahs)
    output=[]
    for i in input_table:
        if i[0] == key :
            for j in range(1,len(i)):
                output.append(i[j])
    return output
