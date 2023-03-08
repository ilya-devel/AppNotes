from control import load_db, get_args
from control.load_db import load_db, import_data
from control.add_note import add_note
from control.save_db import save_db, export
from control.check_id import check_id
from view.show import show_all, show_element
from view.show_msg import show_msg
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
        if ('--all' in args['--show']) or (args['--show'] == dict()):
            show_all(lst_notes=lst_notes)
        if '--id' in args['--show']:
            ind = check_id(ind=args['--show']['--id'], size_lst=len(lst_notes))
            if ind != 'err':
                show_element(elem=lst_notes[ind], ind=ind)

    if '--find' in args:
        find = args['--find']
        lst_args = ''.join([find[key] for key in find.keys()])
        if len(lst_args) != 0:
            find = find_control(args=find, lst_notes=lst_notes)
            if len(find) > 0:
                show_all(find)
        else:
            show_msg("You need to provide an argument. Type --help for help")

    if '--edit' in args:
        indexes = []
        for i in args['--edit']['--edit'].strip().split():
            ind = check_id(i, size_lst=len(lst_notes))
            if ind != 'err':
                indexes.append(ind)
        if len(indexes) > 1:
            show_msg('Only one tab can be edited')
        elif len(indexes) < 1:
            show_msg('Need id of note')
        else:
            title = args['--edit']['--title'] if '--title' in args['--edit'].keys() else ''
            msg = args['--edit']['--msg'] if '--msg' in args['--edit'].keys() else ''
            if title != '' or msg != '':
                lst_notes[indexes[0]].edit_note(title=title, msg=msg)
            else:
                show_msg("You need to fill in the keys --title and --msg")

    if '--delete' in args:
        indexes = []
        for i in args['--delete']['--delete'].strip().split():
            ind = check_id(i, size_lst=len(lst_notes))
            if ind != 'err':
                indexes.append(ind)
        indexes.sort(reverse=True)
        if len(indexes) == 0:
            show_msg("You need enter id of note. Type --help for help")
        for i in indexes:
            print(i)
            show_msg(f"Removed note: {str(lst_notes.pop(i))}")

    if '--export' in args:
        export()

    if '--import' in args:
        import_data(path_ex=args['--import']['--import'], cur_notes=lst_notes)
        pass
