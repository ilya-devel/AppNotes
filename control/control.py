from control import is_db, get_args
from control.add_note import add_note
from control.save_db import save_db
from control.check_id import check_id
from view.show import show_all, show_element


def run_app(argv: list):
    lst_notes = is_db.is_db()
    args = get_args.get_args(argv)

    if len(args.keys()) == 0:
        with open('help.txt', 'r', encoding='UTF-8') as f:
            print(f.read())
        return 0

    work_with_keys(lst_notes, args)

    save_db(lst_notes)


def work_with_keys(lst_notes, args):
    if '--add' in args:
        add_note(lst_notes, args['--add'])
    if '--show' in args:
        if '--all' in args['--show']:
            show_all(lst_notes)
        if '--id' in args['--show']:
            ind = check_id(args['--show']['--id'], len(lst_notes))
            if ind != 'err':
                show_element(lst_notes[ind], ind)

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
