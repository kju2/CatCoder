from __future__ import print_function

def main():
    """
    """
    """
    >>> print(main(*parse_input(".1")))
    """
    pass

def block_overlap(input_string):
    """
    >>> print(block_overlap("0 h 2 3 5 1 v 4 1 5"))
    true
    >>> print(block_overlap("0 h 2 3 5 1 h 4 1 2"))
    false
    >>> print(block_overlap("0 h 2 3 5 1 h 3 3 2"))
    true
    >>> print(block_overlap("0 h 2 3 1 1 h 2 3 1"))
    true
    >>> print(block_overlap("0 h 2 3 5 1 v 3 1 1"))
    false
    >>> print(block_overlap("0 h 2 3 5 1 v 3 1 3"))
    true
    >>> print(block_overlap("0 h 8 7 2 1 v 10 7 6"))
    false
    >>> print(block_overlap("0 h 2 3 5 1 v 3 1 2"))
    false
    >>> print(block_overlap("0 h 4 3 3 2 v 6 2 2"))
    true
    >>> print(block_overlap("0 v 3 3 2 1 v 3 5 2"))
    false
    >>> print(block_overlap("0 h 1 3 2 1 h 5 3 2"))
    false
    """
    input_string = input_string.split(' ')
    blocks = []
    for i in range(2):
        b_id = int(input_string.pop(0))
        orientation = input_string.pop(0)
        x = int(input_string.pop(0))
        y = int(input_string.pop(0))
        l = int(input_string.pop(0))
        blocks.append(Block(b_id, orientation, x, y, l))

    return str(blocks[0].overlaps(blocks[1])).lower()

def parse_input(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    pass

class Block:

    def __init__(self, b_id, orientation, x, y, l):
        self.b_id = b_id
        self.orientation = orientation
        self.x = x
        self.y = y
        self.l = l

    def crosses(self, other_x, other_y):
        curr_x = self.x
        curr_y = self.y

        for i in range(self.l):
            if curr_x == other_x and curr_y == other_y:
                return True

            if self.orientation == 'v':
                curr_y += 1
            else:
                curr_x += 1

        return False

    def overlaps(self, b2):
        curr_x = self.x
        curr_y = self.y

        for i in range(self.l):
            if b2.crosses(curr_x, curr_y):
                return True
            else:
                if self.orientation == 'v':
                    curr_y += 1
                else:
                    curr_x += 1
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
