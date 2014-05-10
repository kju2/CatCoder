from __future__ import print_function

def caluclate_initial_fund(n, start, end, funds):
    """
    >>> caluclate_initial_fund(3, 2, 3, [20, 30, 10])
    40
    >>> caluclate_initial_fund(4, 2, 3, [40, -10, 20, 30])
    10
    >>> caluclate_initial_fund(*parse_input("input.1"))
    -96
    >>> caluclate_initial_fund(*parse_input("input.2"))
    -949
    >>> caluclate_initial_fund(*parse_input("input.3"))
    -39
    >>> caluclate_initial_fund(*parse_input("input.4"))
    -248
    >>> caluclate_initial_fund(*parse_input("input.5"))
    -333
    >>> caluclate_initial_fund(*parse_input("input.6"))
    -267
    """
    """
    """
    return sum(funds[start - 1 : end])

def parse_input(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    line = map(int, lines[0].split(' '))
    n = line.pop(0)
    start = line.pop(0)
    end = line.pop(0)
    funds = line[:]
    return n, start, end, funds

if __name__ == "__main__":
    import doctest
    doctest.testmod()
