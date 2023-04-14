from start_end import start_notes
from menu import menu
from controller import process_flow

notes_list = start_notes()

menu_key = 'Главное меню'
menu_item = menu[menu_key]

while not isinstance(menu_item, tuple) or menu_item[0] != 'Выход':
    menu_item, menu_key = process_flow(notes_list, menu_item, menu_key)