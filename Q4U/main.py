from __future__ import print_function

def calculate_max_initial_fund(n, funds):
    """
    >>> print(calculate_max_initial_fund(10, [-3, 5, 2, -1, 3, -10, 4, 5, -2, -1]))
    9
    >>> print(calculate_max_initial_fund(*parse_input("input.1")))
    26314
    >>> print(calculate_max_initial_fund(*parse_input("input.2")))
    226843
    >>> print(calculate_max_initial_fund(*parse_input("input.3")))
    9024192
    >>> print(calculate_max_initial_fund(*parse_input("input.4")))
    24023857
    >>> print(calculate_max_initial_fund(*parse_input("input.5")))
    25019396
    >>> print(calculate_max_initial_fund(*parse_input("input.6")))
    24840859
    """
    max_ending_here = max_so_far = 0
    for x in funds:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

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
