from control import *
from control import is_db, get_args
from control.add_note import add_note
from control.save_db import save_db
from view.show_all import show_all


def run_app(argv: list):
    lst_notes = is_db.is_db()
    print('DB loaded')
    args = get_args.get_args(argv)
    print('Get args')

    if len(args.keys()) == 0:
        with open('help.txt', 'r', encoding='UTF-8') as f:
            print(f.read())
        return 0

    work_with_keys(lst_notes, args)

    print(args)
    print(lst_notes)

    save_db(lst_notes)


def work_with_keys(lst_notes, args):
    if '--add' in args:
        add_note(lst_notes, args['--add'])
    if '--show' in args:
        if '--all' in args['--show']:
            show_all(lst_notes)
        if '--id' in args['--show']:
            id = args['--show']['--id']
            id = int(id) if (id.is_digit) else "ERROR"

    if '--find' in args:
        pass
    if '--edit' in args:
        pass
    if '--delete' in args:
        pass
    if '--export' in args:
        pass
    if '--import' in args:
        pass
