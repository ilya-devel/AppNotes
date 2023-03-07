from datetime import datetime
import control.is_db


def save_db(lst_notes:list):
    '''
    Saving database
    :param lst_notes: list of notes
    :return:
    '''
    try:
        with open(control.is_db.FILE_DB, 'a', encoding='UTF-8') as file:
            for note in lst_notes:
                file.write(f'{note.__str__()}\n')
        return 0
    except Exception as err:
        with open('log_err.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}\t[ERROR]\t{err}')
