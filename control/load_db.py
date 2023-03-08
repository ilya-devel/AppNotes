import os
from control.settings import FILE_DB
from classes.note import Note
from control.write_log import write_log
from view.show_msg import show_msg
from view.show_err import show_err


def load_db():
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


def import_data(path_ex: str, cur_notes: list):
    path_ex = path_ex.strip()
    str_cur_notes = [str(note) for note in cur_notes]
    if os.path.isfile(path_ex):
        try:
            with open(path_ex, 'r', encoding='UTF-8') as file:
                for row in file.readlines():
                    if row.strip() != '' and len(row.split(';')) == 4:
                        tmp = Note()
                        tmp.from_db(row, len(cur_notes))
                        if str(tmp) in str_cur_notes:
                            show_msg("Database has this note")
                        else:
                            cur_notes.append(tmp)
        except Exception as err:
            show_err(f'Path is not valid: {err}')
    else:
        show_msg(f'Path is not valid: {path_ex}')
