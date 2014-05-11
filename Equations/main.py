from __future__ import print_function

transformations = {0: [6,9], 1: [], 2: [3], 3: [2, 5], 5: [3], 6: [0, 9], 8: [], 9: [0, 6]}

def parse_equation(eq_str):
    eq = list(eq_str)
    for i in range(len(eq)):
        c = eq[i]
        if c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            eq[i] = int(c)
    return eq

def concat_eq(eq):
    output = ""
    for x in eq:
        output += str(x)
    return output

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
    eq = parse_equation(info)
    ls = eq[0]
    rs = eq[2]
    if ls in transformations and rs in transformations[ls]:
        return str(ls) + '=' + str(ls)
    if rs in transformations and ls in transformations[rs]:
        return str(rs) + '=' + str(rs)
    return None


def level2(info):
    """
    >>> print(level2("0+3=9"))
    6+3=9
    >>> print(level2("8=2+9"))
    8=2+6
    >>> print(level2("1+5=0"))
    1+5=6
    """
    """
    """
    eq = parse_equation(info)
    plus = eq.index('+')
    if plus == 1:
        def check(eq):
            return eq[0] + eq[2] == eq[4]
    else:
        def check(eq):
            return eq[2] + eq[4] == eq[0]

    trans_op = []
    for n in (eq[0], eq[2], eq[4]):
        for t in transformations[n]:
            trans_op.append((n, t))

    for (n, t) in trans_op:
        pos = eq.index(n)
        eq[pos] = t

        if check(eq):
            break
        else:
            eq[pos] = n

    return concat_eq(eq)

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
