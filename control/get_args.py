from control.set_args import set_args

def get_args(args:list):
    if len(args) == 0 or '--help' in args:
        with open('help.txt', 'r', encoding='UTF-8') as f:
            print(f.read())
        return 0
    else:
        set_args(args)