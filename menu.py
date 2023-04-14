from outputs import all_notes, note_by_date, note_by_id
from edits import add_note, update_note, delete_note
from start_end import finish_notes


def view_note_by_date(notes_list):
    date = input('Введите дату dd.mm.YYYY : ')
    notes = note_by_date(date, notes_list)
    if notes:
        for note in notes:
            print(note)
    else:
        print("Нет такой даты")


def view_note_by_id(notes_list):
    note_id = input('Введите id заметки ')
    note = note_by_id(note_id, notes_list)
    if note:
        print(note)
    else:
        print('Нет такого id')


def exit_notes(notes_list):
    finish_notes(notes_list)
    return ('Выход', None), None


def to_main_nenu(notes_list):
    menu_key = 'Главное меню'
    menu_item = menu[menu_key]
    return menu_item, menu_key


def to_view_menu(notes_list):
    menu_key = 'Меню просмотра'
    menu_item = menu[menu_key]
    return menu_item, menu_key


def to_edit_menu(notes_list):
    menu_key = 'Меню редактирования'
    menu_item = menu[menu_key]
    return menu_item, menu_key



main_menu = {
    '1': ('Просмотреть заметки', to_view_menu),
    '2': ('Редактировать заметки', to_edit_menu),
    '0': ('Выход', exit_notes)
}

view_menu = {
    '1': ('Просмотреть все', all_notes),
    '2': ('Найти по дате', view_note_by_date),
    '3': ('Найти по id', view_note_by_id),
    '0': ('Выход', to_main_nenu)
}

edit_menu = {
    '1': ('Добавить запись', add_note),
    '2': ('Редактировать запись', update_note),
    '3': ('Удалить запись', delete_note),
    '0': ('Выход', to_main_nenu)
}

menu = {
    'Главное меню': main_menu,
    'Меню просмотра': view_menu,
    'Меню редактирования': edit_menu
}


def print_menu(item, item_key):
    print()
    print(item_key)
    for key in item.keys():
        print(key + ' ' + item[key][0])

