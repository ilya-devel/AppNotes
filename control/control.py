from control.get_args import get_args
from control.is_db import is_db
from control.save_db import save_db


def run_app(argv: list):
    lst_notes = is_db()
    args = get_args(argv)

    if len(args.keys()) == 0:
        with open('help.txt', 'r', encoding='UTF-8') as f:
            print(f.read())
        return 0

    print(args)

    save_db(lst_notes)
