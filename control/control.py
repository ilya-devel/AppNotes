from control.get_args import get_args


def run_app(argv: list):
    args = get_args(argv)
    if len(args.keys()) == 0:
        with open('help.txt', 'r', encoding='UTF-8') as f:
            print(f.read())
        return 0
