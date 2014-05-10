from __future__ import print_function

def calculate_max_initial_fund(n, funds):
    """
    >>> print(calculate_max_initial_fund(10, [-3, 5, 2, -1, 3, -10, 4, 5, -2, -1]))
    9 2 2 5 7 8
    >>> print(calculate_max_initial_fund(*parse_input("input.1")))
    180 2 3 3 8 8
    >>> print(calculate_max_initial_fund(*parse_input("input.2")))
    175 2 2 3 7 7
    >>> print(calculate_max_initial_fund(*parse_input("input.3")))
    605 2 9 18 22 29
    >>> print(calculate_max_initial_fund(*parse_input("input.4")))
    1902 2 63 80 123 187
    >>> print(calculate_max_initial_fund(*parse_input("input.5")))
    1359 2 47 70 90 149
    >>> print(calculate_max_initial_fund(*parse_input("input.6")))
    1556 2 30 68 129 147
    """
    """
    """
    max_initial_fund = 0
    possibilities = []

    for i in range(len(funds) - 1):
        for j in range(i, len(funds) + 1):
            sum_funds = sum(funds[i:j])
            if sum_funds == max_initial_fund:
                possibilities.append((i, j))
            if sum_funds > max_initial_fund:
                possibilities = [(i, j)]
                max_initial_fund = sum_funds
    output = str(max_initial_fund) + ' ' + str(len(possibilities))
    for (i, j) in possibilities:
        output += ' ' + str(i + 1) + ' ' + str(j)

    return output

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
