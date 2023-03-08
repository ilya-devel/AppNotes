from view.show_err import show_err


def check_id(ind: str, size_lst: int):
    if not ind.strip().isdigit():
        show_err(f"Unknown index {ind}")
        return 'err'
    if int(ind) >= size_lst or int(ind) < 0:
        show_err(f"Index out of range: {ind}")
        return 'err'
    return int(ind.strip())
