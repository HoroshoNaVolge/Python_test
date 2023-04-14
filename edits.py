from models import Notes
from outputs import all_notes


def add_note(notes_list):
    try:
        max_id = max(map(lambda x: x.note_id, notes_list))
    except:
        max_id = 0
    title, text = input_note()
    note = Notes(max_id, title, text)
    notes_list.append(note)


def delete_note(notes_list):
    all_notes(notes_list)
    note_id = input('Chose id of note which you want to delete from previous list: ')
    note = list(filter(lambda x: x.note_id == int(note_id), notes_list))
    if len(note) == 1:
        note = note[0]
        notes_list.remove(note)
    else:
        print("!!! id Doesn't exist !!!")

def update_note(notes_list):
    all_notes(notes_list)
    note_id = input('Chose id of note which you want to edit from previous list: ')
    note = list(filter(lambda x: x.note_id == int(note_id), notes_list))
    if len(note) == 1:
        note = note[0]
        title, text = input_note()
        note.note_edit(title, text)
    else:
        print("!!! id Doesn't exist !!!")


def input_note():
    title = input('Input title not longer than 14 characters: ')[0:14]
    note_text = input('Input new text: ')
    return title, note_text

