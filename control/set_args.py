def set_args(args: list):
    """
    Function for arguments handling
    :param args: list of arguments
    :return:
    """
    lst_args = dict()
    main_key = ''
    tmp_key = ''
    for i in range(len(args)):

        if args[i] in ['--add', '--show', '--find', '--edit', '--delete', '--export', '--import']:
            if tmp_key != '':
                lst_args[main_key][tmp_key] = lst_args[main_key][tmp_key].strip()
            main_key = args[i]
            lst_args[main_key] = dict()
            tmp_key = ''
            if main_key in ['--find', '--edit']:
                tmp_key = main_key
                lst_args[main_key][tmp_key] = ''
            continue

        if args[i].startswith('--'):
            tmp_key = args[i]
            lst_args[main_key][tmp_key] = ''
        else:
            lst_args[main_key][tmp_key] += f'{args[i]} '

    return lst_args
