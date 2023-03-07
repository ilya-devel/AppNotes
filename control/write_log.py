from datetime import datetime


def write_log(type_msg: str, msg: str):
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}\t[{type_msg.upper()}]\t{msg}\n')
