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

    game = Game(width, heigh, blocks)

    for e in events:
        if game.move(blocks[e[0]], e[1]) == False:
            return str(True).lower()

    return str(False).lower()

def is_moveable(input_string):
    """
    >>> print(is_moveable("6 5 3 0 h 2 3 3 1 h 1 5 6 2 v 6 1 3"))
    1
    >>> print(is_moveable("6 5 3 0 h 2 3 3 1 h 1 5 6 2 v 6 1 3"))
    1
    >>> print(is_moveable("6 6 12 0 h 3 4 2 1 v 1 4 3 2 h 1 3 2 3 v 2 1 2 4 v 4 5 2 5 h 3 3 2 6 h 3 2 2 7 h 4 1 2 8 h 5 6 2 9 v 5 3 3 10 v 6 3 3 11 h 5 2 2"))
    1 2 3 4 5 6 8 9 10 11
    >>> print(is_moveable("6 6 12 0 h 3 4 2 1 h 2 3 2 2 h 1 1 3 3 h 1 2 3 4 v 1 3 2 5 v 1 5 2 6 v 3 5 2 7 h 4 6 3 8 v 4 1 2 9 h 4 3 2 10 v 5 4 2 11 v 6 4 2"))
    1 2 3 4 5 6 7 8 10
    >>> print(is_moveable("6 6 10 0 h 3 4 2 1 h 5 2 2 2 v 1 5 2 3 h 3 5 3 4 v 4 2 2 5 h 5 6 2 6 v 2 4 3 7 v 6 3 3 8 h 1 3 2 9 h 1 1 2"))
    1 3 6 7
    >>> print(is_moveable("12 12 49 0 h 3 4 2 1 h 5 2 2 2 v 1 5 2 3 h 3 5 3 4 v 4 2 2 5 h 5 6 2 6 v 2 4 3 7 v 6 3 3 8 h 2 3 2 9 h 1 1 2 10 v 3 7 2 11 h 3 10 3 12 h 3 11 2 13 h 3 9 2 14 h 5 9 3 15 h 10 9 3 16 h 8 9 2 17 v 1 10 3 18 v 2 11 2 19 h 3 12 2 20 h 6 12 2 21 h 10 12 2 22 v 5 11 2 23 v 6 10 2 24 v 8 10 3 25 v 9 10 3 26 v 12 10 3 27 v 12 4 5 28 v 11 4 5 29 v 10 3 5 30 v 9 4 4 31 h 9 8 2 32 v 8 6 3 33 v 8 2 4 34 v 7 4 5 35 v 11 10 2 36 v 2 7 2 37 v 2 9 2 38 v 1 7 3 39 h 3 6 2 40 v 1 3 2 41 v 9 2 2 42 v 7 1 3 43 v 5 3 2 44 h 3 1 4 45 h 1 2 3 46 h 8 1 5 47 h 11 3 2 48 h 10 2 3"))
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
    >>> print(is_moveable("7 5 6 0 h 1 2 2 1 v 3 1 4 2 h 2 5 3 3 h 6 4 2 4 h 4 3 3 5 v 7 1 3"))
    0 1 4 5
    >>> print(is_moveable("12 12 23 0 h 8 7 2 1 v 10 7 6 2 v 4 5 4 3 v 2 7 3 4 v 9 1 3 5 v 5 4 3 6 h 7 6 3 7 h 5 8 3 8 h 10 6 2 9 h 2 2 4 10 h 1 3 2 11 v 1 4 4 12 v 3 4 3 13 v 2 4 2 14 v 3 8 3 15 v 4 9 4 16 v 6 9 4 17 h 7 11 3 18 h 7 10 3 19 h 5 7 3 20 h 6 5 5 21 h 6 4 5 22 h 5 3 4"))
    0 1 4 5 15 16 17 18 19
    """
    """
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

    game = Game(width, heigh, blocks)
    unmoveable = ""
    for b in blocks:
        if game.is_moveable(b) == False:
            unmoveable += str(b.b_id) + " "

    return unmoveable.rstrip()

def find_clash(input_string):
    """
    >>> print(find_clash("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 3 4 0 1 2 -1 2 3 0 1"))
    2
    >>> print(find_clash("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 3 2 2 -1 0 5"))
    1
    >>> print(find_clash("6 6 12 0 h 3 4 2 1 v 1 4 3 2 h 1 3 2 3 v 2 1 2 4 v 4 5 2 5 h 3 3 2 6 h 3 2 2 7 h 4 1 2 8 h 5 6 2 9 v 5 3 3 10 v 6 3 3 11 h 5 2 2 11 0 -1 4 -1 8 -3 4 1 9 1 10 1 0 1 5 2 2 2 3 4 5 -1"))
    9
    >>> print(find_clash("6 6 8 0 h 1 4 2 1 h 1 3 2 2 v 2 1 2 3 v 3 4 2 4 v 3 2 2 5 h 3 1 2 6 v 4 3 3 7 v 5 3 3 19 3 1 6 1 7 1 5 2 4 -1 1 4 6 -3 0 2 2 4 0 -2 6 3 1 -4 6 -3 4 2 6 3 5 -4 4 -2 6 -3 7 -3"))
    19
    >>> print(find_clash("7 5 6 0 h 1 2 2 1 v 3 1 4 2 h 2 5 3 3 h 6 4 2 4 h 4 3 3 5 v 7 1 3 13 3 -1 3 -1 3 1 5 2 2 2 1 1 3 -1 5 -1 2 1 0 1 1 -1 3 -1 5 3"))
    9
    >>> print(find_clash("12 12 16 0 h 5 3 2 1 v 1 3 4 2 h 5 5 3 3 h 2 5 2 4 h 2 4 3 5 v 4 1 3 6 v 7 2 3 7 v 7 6 5 8 h 1 10 3 9 h 5 11 4 10 h 4 7 3 11 h 11 7 2 12 h 9 5 3 13 h 9 3 4 14 v 10 8 4 15 v 2 7 2 11 6 -1 4 4 12 1 15 1 8 3 15 3 9 -2 1 6 5 3 0 -3 4 -1"))
    11
    >>> print(find_clash("11 12 16 0 h 2 3 2 1 v 1 8 4 2 h 5 5 3 3 h 2 5 2 4 h 5 4 3 5 v 4 4 3 6 v 7 1 3 7 v 7 6 5 8 h 4 10 3 9 h 3 11 4 10 h 4 7 3 11 h 10 7 2 12 h 9 5 3 13 h 8 3 4 14 v 10 8 4 15 v 2 10 2 7 15 -3 8 -2 11 -2 12 -1 14 -2 9 4 14 2"))
    6
    """
    """
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
    game.pop(0)
    while len(game) > 0:
        events.append((int(game.pop(0)), int(game.pop(0))))

    game = Game(width, heigh, blocks)
    for i in range(len(events)):
        b, steps = events[i]
        if game.move(blocks[b], steps) is False:
            return i
    return len(events)
    
class Game:

    def __init__(self, width, height, blocks):
        self.width = width
        self.height = height
        self.blocks = blocks

    def is_moveable(self, b):
        if self.move(b, 1):
            self.move(b, -1)
            return True
        self.move(b, -1)
        if self.move(b, -1):
            self.move(b, 1)
            return True
        self.move(b, 1)
        return False

    def _try_move(self, b):
        b.move_forward()
        if self.valid() is False:
            b.move_backward()
            return False

        b.move_backward()
        if self.valid() is False:
            b.move_forward()
            return False

        return True

    def valid(self):
        for b1 in self.blocks:
            if b1.x < 0 or b1.y < 0:
                return False

            if b1.orientation == 'h':
                if b1.x + b1.l > self.width:
                    return False
            else:
                if b1.y + b1.l > self.height:
                    return False

        for b1 in self.blocks:
            for b2 in self.blocks:
                if b1 == b2:
                    continue

                if b1.clashes_with(b2):
                    return False

        return True


    def move(self, b, steps):
        movement = steps / abs(steps)
        for s in range(abs(steps)):
            b.move(movement)
            if self.valid() is False:
                return False

        return True

class Block:

    def __init__(self, b_id, orientation, x, y, l):
        self.b_id = b_id
        self.orientation = orientation
        self.x = x
        self.y = y
        self.l = l

    def move(self, step):
        movement = 1
        if step < 0:
            movement = -1

        if self.orientation == 'h':
            self.x += movement
        else:
            self.y += movement

    def move_forward(self):
        self.move(1)

    def move_backward(self):
        self.move(-1)

    def clashes_with(self, other_b):
        x = self.x
        y = self.y
        for i in range(self.l):
            if other_b.is_on(x, y):
                return True

            if self.orientation == 'h':
                x += 1
            else:
                y += 1

        return False

    def is_on(self, other_x, other_y):
        x = self.x
        y = self.y
        for i in range(self.l):
            if x == other_x and y == other_y:
                return True

            if self.orientation == 'h':
                x += 1
            else:
                y += 1

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

    return str(blocks[0].clashes_with(blocks[1])).lower()

def parse_input(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    pass

if __name__ == "__main__":
    #print(main("6 5 3 0 h 2 3 3 1 h 2 5 5 2 v 6 2 2 0 -2"))
    import doctest
    doctest.testmod()
