import os
from control.settings import FILE_DB
from classes.note import Note
from control.write_log import write_log




def is_db():
    lst_notes = []
    if os.path.isfile(FILE_DB):
        with open(FILE_DB, 'r', encoding='UTF-8') as file:
            for row in file.readlines():
                if row.strip() != '' and len(row.split(';')) == 4:
                    tmp = Note()
                    tmp.from_db(row, len(lst_notes))
                    lst_notes.append(tmp)
    else:
        err = 'Database is corrupted or missing'
        print(err)
        msg = 'Create new database'
        print(msg)
        write_log('ERROR', err)
        write_log('DEBUG', msg)
    return lst_notes
