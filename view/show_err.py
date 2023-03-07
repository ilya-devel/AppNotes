from control.write_log import write_log


def show_err(msg: str):
    print(msg)
    write_log('ERROR', msg)
