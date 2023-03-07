from classes.note import Note
from control.write_log import write_log


def add_note(lst_notes: list, args: dict):
    if '--title' and '--msg' in args.keys():
        if args['--title'] or args['--msg'] != '':
            tmp = Note()
            tmp.add_note(args['--title'], args['--msg'])
            lst_notes.append(tmp)
        else:
            msg = 'You send empty title or msg'
            print(msg)
            write_log('ERROR', msg)
    else:
        msg = 'You don\'t get title and message'
        print(msg)
        write_log('DEBUG', msg)
