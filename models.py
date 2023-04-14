import datetime


class Notes:

    def __init__(self, *args):
        '''
        :param args:
        0 — note id
        1 — note title
        2 — note text
        '''
        if len(args) == 3:
            self.note_id = args[0] + 1
            self.title = args[1]
            self.text = args[2]
            self.date = datetime.date.today()
            self.time = datetime.datetime.now().time()
        elif len(args[0]) == 5:
            self.note_id = int(args[0][0])
            self.title = args[0][1]
            self.text = args[0][2]
            self.date = datetime.datetime.strptime(args[0][3], '%d.%m.%Y').date()
            self.time = datetime.time.fromisoformat(args[0][4])
        else:
            print('error')

    def __repr__(self):
        return str(self.note_id) + ' ' + datetime.datetime.strftime(self.date,
                                                                    '%d.%m.%Y') + ' ' + self.title + ' ' + self.text

    def __str__(self):
        return str(self.note_id) + ' | ' + datetime.datetime.strftime(self.date, '%d.%m.%Y') + ' | ' + self.title + (
                    14 - len(self.title)) * ' ' + ' | ' + self.text

    def note_edit(self, title, text):
        self.title = title
        self.text = text
        self.date = datetime.date.today()
        self.time = datetime.datetime.now().time()

    def to_csv(self):
        return str(self.note_id) + ';' + self.title + ';' + self.text + ';' + \
            datetime.datetime.strftime(self.date, '%d.%m.%Y') + ';' + datetime.time.strftime(self.time,
                                                                                             '%H:%M:%S') + '\n'
