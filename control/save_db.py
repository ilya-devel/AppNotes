from control.settings import FILE_DB
from control.write_log import write_log


def save_db(lst_notes: list):
    '''
    Saving database
    :param lst_notes: list of notes
    :return: process complete
    '''
    try:
        with open(FILE_DB, 'w', encoding='UTF-8') as file:
            for note in lst_notes:
                file.write(f'{str(note).strip()}\n')
    except Exception as err:
        write_log('ERROR', str(err))
    return 0
