import os
from datetime import datetime

from classes.note import Note

FILE_DB = 'db.csv'


def is_db():
    lst_notes = []
    if os.path.isfile(FILE_DB):
        with open(FILE_DB, 'r', encoding='UTF-8') as file:
            for row in file.readlines():
                lst_notes.append(Note.from_db(row, len(lst_notes)))
    else:
        err = 'Database is corrupted or missing'
        print(err)
        msg = 'Create new database'
        print(msg)
        with open('log_err.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}\t[ERROR]\t{err}')
            file.write(f'{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}\t[DEBUG]\t{msg}')

    return lst_notes
