from __future__ import print_function

def calculate_max_initial_fund(n, funds):
    """
    >>> calculate_max_initial_fund(10, [2, 3, 4, -12, 3, 2, -4, 5, 6, -1])
    12
    >>> calculate_max_initial_fund(*parse_input("input.1"))
    580
    >>> calculate_max_initial_fund(*parse_input("input.2"))
    722
    >>> calculate_max_initial_fund(*parse_input("input.3"))
    2566
    >>> calculate_max_initial_fund(*parse_input("input.4"))
    3207
    >>> calculate_max_initial_fund(*parse_input("input.5"))
    7332
    >>> calculate_max_initial_fund(*parse_input("input.6"))
    5541
    """
    """
    """
    max_initial_fund = 0
    for i in range(len(funds) - 1):
        for j in range(i, len(funds) + 1):
            if max_initial_fund < sum(funds[i:j]):
                max_initial_fund = max(max_initial_fund, sum(funds[i:j]))
    return max_initial_fund

def parse_input(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    line = map(int, lines[0].split(' '))
    n = line.pop(0)
    funds = line[:]
    return n, funds

if __name__ == "__main__":
    import doctest
    doctest.testmod()
