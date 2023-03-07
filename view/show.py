import operator


def split_string(txt: str, size: int):
    list_str = []
    tmp_str = ''
    for word in txt.split():
        if len(tmp_str + word + ' ') < size:
            tmp_str += f'{word} '
        elif len(word) >= size:
            if tmp_str != '':
                list_str.append(tmp_str)
                tmp_str = ''
            list_str.append(word)
        else:
            list_str.append(tmp_str)
            tmp_str = ''
    if tmp_str != '':
        list_str.append(tmp_str)
    return list_str


def show_element(elem, ind: int):
    print(f'{"id":^5} | '
          f'{"Date Create":^21} | '
          f'{"Title":^30} | '
          f'{"Message":^50} | '
          f'{"Date Edit":^21}')
    print(f'{"=" * 6}+{"=" * 23}+{"=" * 32}+{"=" * 52}+{"=" * 21}')
    dc, tit, msg, de = str(elem).strip().split(';')
    if len(tit) < 30 or len(msg) < 50:
        print(f'{ind:^5} | '
              f'{dc:^21} | '
              f'{tit:^30} | '
              f'{msg:^50} | '
              f'{de:^21}')
    else:
        lst_tit = split_string(tit, 28)
        lst_msg = split_string(msg, 48)
        max_size = len(lst_msg) if len(lst_msg) > len(lst_tit) else len(lst_tit)
        print(f'{ind:^5} | '
              f'{dc:^21} | '
              f'{lst_tit[0]:^30} | '
              f'{lst_msg[0]:^50} | '
              f'{de:^21}')
        for ind in range(1, max_size):
            print(f'{" ":^5} | '
                  f'{" ":^21} | '
                  f'{lst_tit[ind] if ind < len(lst_tit) else " ":^30} | '
                  f'{lst_msg[ind] if ind < len(lst_msg) else " ":^50} | '
                  f'{" ":^21}')
    print(f'{"-" * 6}+{"-" * 23}+{"-" * 32}+{"-" * 52}+{"-" * 21}')


def show_all(lst_notes: list):
    lst_notes.sort()
    print(f'{"id":^5} | '
          f'{"Date Create":^21} | '
          f'{"Title":^30} | '
          f'{"Message":^50} | '
          f'{"Date Edit":^21}')
    print(f'{"=" * 6}+{"=" * 23}+{"=" * 32}+{"=" * 52}+{"=" * 21}')
    for i in range(len(lst_notes)):
        dc, tit, msg, de = str(lst_notes[i]).strip().split(';')
        if len(tit) < 30 or len(msg) < 50:
            print(f'{lst_notes[i].id:^5} | '
                  f'{dc:^21} | '
                  f'{tit:^30} | '
                  f'{msg:^50} | '
                  f'{de:^21}')
        else:
            lst_tit = split_string(tit, 28)
            lst_msg = split_string(msg, 48)
            max_size = len(lst_msg) if len(lst_msg) > len(lst_tit) else len(lst_tit)
            print(f'{lst_notes[i].id:^5} | '
                  f'{dc:^21} | '
                  f'{lst_tit[0]:^30} | '
                  f'{lst_msg[0]:^50} | '
                  f'{de:^21}')
            for ind in range(1, max_size):
                print(f'{" ":^5} | '
                      f'{" ":^21} | '
                      f'{lst_tit[ind] if ind < len(lst_tit) else " ":^30} | '
                      f'{lst_msg[ind] if ind < len(lst_msg) else " ":^50} | '
                      f'{" ":^21}')
        print(f'{"-" * 6}+{"-" * 23}+{"-" * 32}+{"-" * 52}+{"-" * 21}')
