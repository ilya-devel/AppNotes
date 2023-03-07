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

    @staticmethod
    def from_db(params=str, id=int):
        tmp = Note()
        tmp.id = id
        tmp.date_create, tmp.title, tmp.msg, tmp.date_edit = params.split(';')
        return tmp

    def __str__(self) -> str:
        return f'{self.date_create};{self.title};{self.msg};{self.date_edit}'
