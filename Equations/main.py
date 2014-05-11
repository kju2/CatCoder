from __future__ import print_function
from itertools import permutations

change_trans = {0: [6,9], 1: [], 2: [3], 3: [2, 5], 5: [3], 6: [0, 9], 8: [], 9: [0, 6]}
remove_trans = {6: [5], 7: [1], 8: [0, 6, 9], 9: [3, 5], '+': ['-'], '=': ['-']}
add_trans = {0: [8], 1: [7], 3: [9], 5: [6, 9], 6: [8], 9: [8], '-': ['=', '+']}

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

def eval_eq(eq):
    eq = concat_eq(eq)
    if eq.count('=') != 1:
        return False
    return eval(eq.replace("=", "=="))

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
    if ls in change_trans and rs in change_trans[ls]:
        return str(ls) + '=' + str(ls)
    if rs in change_trans and ls in change_trans[rs]:
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
    ns = [x for x in eq if isinstance(x, int)]

    plus = eq.index('+')
    if plus == 1:
        def check(eq):
            return eq[0] + eq[2] == eq[4]
    else:
        def check(eq):
            return eq[2] + eq[4] == eq[0]

    trans_ops = []
    for n in ns:
        trans_ops.extend(change_transformations(n))

    for (n, t) in trans_ops:
        pos = eq.index(n)
        eq[pos] = t

        if check(eq):
            break
        else:
            eq[pos] = n

    return concat_eq(eq)

def change_transformations(n):
    trans_ops = []
    if n in change_trans:
        for t in change_trans[n]:
            trans_ops.append((n, t))
    return trans_ops

def level3(info):
    """
    >>> print(level3("2+6=1"))
    2+5=7
    >>> print(level3("8+3=9"))
    0+9=9
    >>> print(level3("8-6=-8"))
    0-8=-8
    >>> print(level3("1=2+6"))
    7=2+5
    """
    eq = parse_equation(info)
    ns = [x for x in eq if isinstance(x, int)]

    trans_ops = []
    for n in ns:
        trans_ops.extend(change_transformations(n))

    for (r, a) in permutations(ns, 2):
        if r in remove_trans and a in add_trans:
            for rt in remove_trans[r]:
                for at in add_trans[a]:
                    trans_ops.append((r, rt, a, at))

    orig_eq = eq[:]
    for op in trans_ops:
        eq = orig_eq[:]
        if len(op) == 2:
            pos = eq.index(op[0])
            eq[pos] = op[1]
        else:
            posR = eq.index(op[0])
            posA = eq.index(op[2])
            eq[posR] = op[1]
            eq[posA] = op[3]
        if eval_eq(eq):
            return concat_eq(eq)
    return None

def level4(info):
    """
    >>> print(level3("9+2-3-1=8-4"))
    6+2-3-1=8-4
    >>> print(level3("9+2-5+7=8-2"))
    3+2-6+7=8-2
    >>> print(level3("9+2-3-1=8-4"))
    6+2-3-1=8-4
    """
    pass

def level5(info):
    """
    >>> print(level5("8+3=-1"))
    8-9=-1
    >>> print(level5("3-8=5"))
    3=8-5
    """
    eq = parse_equation(info)
    ns = [x for x in eq if isinstance(x, int)]

    trans_ops = []
    for n in ns:
        trans_ops.extend(change_transformations(n))

    for (r, a) in permutations(eq, 2):
        if r in remove_trans and a in add_trans:
            for rt in remove_trans[r]:
                for at in add_trans[a]:
                    trans_ops.append((r, rt, a, at))

    orig_eq = eq[:]
    for op in trans_ops:
        eq = orig_eq[:]
        if len(op) == 2:
            pos = eq.index(op[0])
            eq[pos] = op[1]
        else:
            posR = eq.index(op[0])
            posA = eq.index(op[2])
            eq[posR] = op[1]
            eq[posA] = op[3]
        if eval_eq(eq):
            return concat_eq(eq)
    return None


def level6(info):
    """
    >>> print(level6("9+8=14"))
    8+6=14
    >>> print(level6("14+9=11"))
    14+3=17
    >>> print(level6("98-60=-22"))
    58-80=-22
    """
    """
    """
    eq = parse_equation(info)
    ns = [x for x in eq if isinstance(x, int)]

    trans_ops = []
    for (r, a) in permutations(eq, 2):
        if r in remove_trans and a in add_trans:
            for rt in remove_trans[r]:
                for at in add_trans[a]:
                    for indexOfR in (i for i, x in enumerate(eq) if x == r):
                        for indexOfA in (i for i, x in enumerate(eq) if x == a):
                            trans_ops.append((indexOfR, rt, indexOfA, at))

    orig_eq = eq[:]
    for op in trans_ops:
        eq = orig_eq[:]
        if len(op) == 2:
            pos = eq.index(op[0])
            eq[pos] = op[1]
        else:
            eq[op[0]] = op[1]
            eq[op[2]] = op[3]
        if eval_eq(eq):
            return concat_eq(eq)
    return None

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
