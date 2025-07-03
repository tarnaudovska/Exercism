SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_sublist(smaller, larger):
    """Return True if `smaller` is a contiguous sublist of `larger`."""
    n = len(smaller)
    if n == 0:
        return True
    for i in range(len(larger) - n + 1):
        if larger[i:i + n] == smaller:
            return True
    return False


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL

