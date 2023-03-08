from control.settings import FILE_DB
from control.write_log import write_log
from os import sep, getcwd
from shutil import copy2
from datetime import datetime
from view.show_msg import show_msg
from view.show_err import show_err


def save_db(lst_notes: list, path=FILE_DB):
    """
    Saving database
    :param lst_notes: list of notes
    :return: process complete
    """
    try:
        with open(FILE_DB, 'w', encoding='UTF-8') as file:
            for note in lst_notes:
                file.write(f'{str(note).strip()}\n')
    except Exception as err:
        show_err(str(err))
    return 0


def export():
    try:
        file_name = datetime.now().strftime("Note_%Y-%m-%d_%H-%M-%S.csv")
        copy2(FILE_DB, f"{getcwd()}{sep}{file_name}")
        show_msg(f"Export complete: {getcwd()}{sep}{file_name}")
    except Exception as err:
        show_err(str(err))
