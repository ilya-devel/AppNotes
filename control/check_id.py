from control.write_log import write_log
from view.show_err import show_err


def check_id(id: str, size_lst: int):
    if not id.isdigit() or (int(id) > size_lst or int(id) < 0):
        show_err(f"Unknown index {id}")
    else:
        return int(id)