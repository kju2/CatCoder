from __future__ import print_function

transformations = {0: [6,9], 2: [3], 3: [2, 5], 5: [3], 6: [0, 9], 9: [0, 6]}

def parse_equation(eq_str):
    parts = eq_str.split('=')
    return int(parts[0]), int(parts[1])

def level1(info):
    """
    >>> print(level1("3=2"))
    3=3
    >>> print(level1("5=3"))
    5=5
    >>> print(level1("6=0"))
    6=6
    >>> print(level1("0=9"))
    0=0
    """
    ls, rs = parse_equation(info)
    if ls in transformations and rs in transformations[ls]:
        return str(ls) + '=' + str(ls)
    if rs in transformations and ls in transformations[rs]:
        return str(rs) + '=' + str(rs)
    return None
        

def level2(info):
    """
    """
    pass

def level3(info):
    """
    """
    pass

def level4(info):
    """
    """
    pass

def level5(info):
    """
    """
    pass

def level6(info):
    """
    """
    pass

def level7(info):
    """
    """
    pass

def parse_input(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
