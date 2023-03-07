from control import load_db, get_args
from control.load_db import load_db
from control.add_note import add_note
from control.save_db import save_db
from control.check_id import check_id
from view.show import show_all, show_element
from control.find_elements import find_control


def run_app(argv: list):
    lst_notes = load_db()
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
            show_all(lst_notes=lst_notes)
        if '--id' in args['--show']:
            ind = check_id(ind=args['--show']['--id'], size_lst=len(lst_notes))
            if ind != 'err':
                show_element(elem=lst_notes[ind], ind=ind)

    if '--find' in args:
        # if args['--find']['--find'] != '':
        find = args['--find']
        find = find_control(args=find, lst_notes=lst_notes)
        if len(find) > 0:
            show_all(find)

        pass
    if '--edit' in args:
        pass
    if '--delete' in args:
        pass
    if '--export' in args:
        pass
    if '--import' in args:
        pass
