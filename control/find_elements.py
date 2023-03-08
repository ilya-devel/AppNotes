from view.show_msg import show_msg


def find_control(args: dict, lst_notes: list):
    lst_find = []
    for key in args.keys():
        if args[key] != '':
            if key == '--find':
                tmp_lst = lst_find if len(lst_find) > 0 else lst_notes
                lst_find = find_all(args[key], tmp_lst)
            if key == '--title':
                tmp_lst = lst_find if len(lst_find) > 0 else lst_notes
                lst_find = find_title(args[key], tmp_lst)
            if key == '--msg':
                tmp_lst = lst_find if len(lst_find) > 0 else lst_notes
                lst_find = find_msg(args[key], tmp_lst)
    return lst_find
    pass


def find_all(substring: str, lst_notes: list):
    lst_find = []
    for el in lst_notes:
        if (substring in el.title.strip()) or (substring in el.msg):
            lst_find.append(el)
    if len(lst_find) == 0:
        show_msg("Nothing Found\n")
    return lst_find


def find_title(substring: str, lst_notes: list):
    lst_find = []
    for el in lst_notes:
        if substring in el.title:
            lst_find.append(el)
    if len(lst_find) == 0:
        show_msg("Nothing Found\n")
    return lst_find


def find_msg(substring: str, lst_notes: list):
    lst_find = []
    for el in lst_notes:
        if substring in el.msg:
            lst_find.append(el)
    if len(lst_find) == 0:
        show_msg("Nothing Found\n")
    return lst_find
