from datetime import datetime


class Note:
    def __init__(self):
        self.id = int()
        self.date_create = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        self.title = str()
        self.msg = str()
        self.date_edit = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    def edit_note(self, title='', msg=''):
        if title != '' or msg != '':
            if title != '':
                self.title = title
            if msg != '':
                self.msg = msg
            self.date_edit = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    def from_db(self, params=str, ind=int):
        self.id = ind
        self.date_create, self.title, self.msg, self.date_edit = params.split(';')

    def add_note(self, title, msg):
        self.title = title
        self.msg = msg

    def __str__(self) -> str:
        return f'{self.date_create};{self.title};{self.msg};{self.date_edit}'

    def __lt__(self, other):
        return self.date_create < other.date_create