import datetime

def note_by_date(date, notes_list):
    try:
        date_check = datetime.datetime.strptime(date, '%d.%m.%Y').date()
        note = list(filter(lambda x: x.date == date_check, notes_list))
        if len(note):
            return note
        else:
            return None
    except:
        return None

def all_notes(notes_list):
    for note in notes_list:
        print(note)

def note_by_id(note_id, notes_list):
    note = list(filter(lambda x: x.note_id == int(note_id), notes_list))
    if len(note) == 1:
        return note[0]
    else:
        return None



