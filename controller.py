from menu import print_menu


def process_flow(note_list, menu_item, menu_key):
    print_menu(menu_item, menu_key)
    print()
    input_key =input('Выберите пункт меню: ')
    if input_key in menu_item.keys():
        if menu_key == 'Главное меню' or input_key == '0':
            menu_item, menu_key = menu_item[input_key][1](note_list)
        else:
            menu_item[input_key][1](note_list)
    else:
        print('Ошибка ввода')
        return menu_item, menu_key
    return menu_item, menu_key