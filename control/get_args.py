from control.set_args import set_args


def get_args(args: list):
    """
    Function checks if arguments were received or not
    :param args: list of arguments
    :return: dict
    """
    if len(args) == 0 or '--help' in args:
        return dict()
    elif '--add' or '--show' or '--find' or '--edit' or '--delete' or '--export' or '--import' not in args:
        print('UNKNOWN ARGUMENTS\n')
        return dict()
    else:
        return set_args(args)

