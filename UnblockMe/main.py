from __future__ import print_function

def main(input_string):
    """
    >>> print(main("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 2 0 2"))
    true
    >>> print(main("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 2 0 1"))
    false
    >>> print(main("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 2 0 -1"))
    false
    >>> print(main("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 2 0 -2"))
    true
    >>> print(main("6 6 12 0 h 3 4 2 1 v 1 4 3 2 h 1 3 2 3 v 2 1 2 4 v 4 5 2 5 h 3 3 2 6 h 3 2 2 7 h 4 1 2 8 h 5 6 2 9 v 5 3 3 10 v 6 3 3 11 h 5 2 2 0 1"))
    true
    >>> print(main("6 6 12 0 h 3 4 2 1 v 1 4 3 2 h 1 3 2 3 v 2 1 2 4 v 4 5 2 5 h 3 3 2 6 h 3 2 2 7 h 4 1 2 8 h 5 6 2 9 v 5 3 3 10 v 6 3 3 11 h 5 2 2 0 -1"))
    false
    >>> print(main("6 6 12 0 h 3 4 2 1 h 2 3 2 2 h 1 1 3 3 h 1 2 3 4 v 1 3 2 5 v 1 5 2 6 v 3 5 2 7 h 4 6 3 8 v 4 1 2 9 h 4 3 2 10 v 5 4 2 11 v 6 4 2 5 -1"))
    true
    >>> print(main("6 6 10 0 h 3 4 2 1 h 5 2 2 2 v 1 5 2 3 h 3 5 3 4 v 4 2 2 5 h 5 6 2 6 v 2 4 3 7 v 6 3 3 8 h 1 3 2 9 h 1 1 2 5 -1"))
    false
    >>> print(main("7 5 6 0 h 1 2 2 1 v 3 1 4 2 h 2 5 3 3 h 6 4 2 4 h 4 3 3 5 v 7 1 3 4 2"))
    true
    """
    """
    >>> print(main(*parse_input(".1")))
    """
    game = input_string.split(' ')
    blocks = []
    width = int(game.pop(0))
    heigh = int(game.pop(0))
    for i in range(int(game.pop(0))):
        b_id = int(game.pop(0))
        orientation = game.pop(0)
        x = int(game.pop(0)) - 1
        y = int(game.pop(0)) - 1
        l = int(game.pop(0))
        blocks.append(Block(b_id, orientation, x, y, l))

    events = []
    while len(game) > 0:
        events.append((int(game.pop(0)), int(game.pop(0))))

    for e in events:
        if blocks[e[0]].move(blocks, e[1]) == False:
            return str(True).lower()

    return str(False).lower()

class Block:

    def __init__(self, b_id, orientation, x, y, l):
        self.b_id = b_id
        self.orientation = orientation
        self.x = x
        self.y = y
        self.l = l

    def move(self, blocks, steps):
        old_x = self.x
        old_y = self.y

        #print(self.b_id, steps, self.x, self.y)
        for i in range(abs(steps)):

            if self.orientation == 'v':
                if steps < 0:
                    self.y -= 1
                else:
                    self.y += 1
            else:
                if steps < 0:
                    self.x -= 1
                else:
                    self.x += 1

            #print(self.b_id, steps, self.x, self.y)
            for b in blocks:
                if (self != b and self.overlaps(b)) or (self.x < 0 or self.y < 0):
                    self.x = old_x
                    self.y = old_y
                    #print(b.b_id)
                    return False

        return True

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

if __name__ == "__main__":
    #print(main("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 2 0 -2"))
    import doctest
    doctest.testmod()
