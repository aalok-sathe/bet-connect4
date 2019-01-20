"""
convention: bottom row first
"""
from color import *

def err():
    print(RED + 'ERR: ' + RESET, file=stderr, end='')
def info():
    print(YELLOW + 'ERR: ' + RESET, file=stderr, end='')

# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

class Board:
    R = None
    C = None
    board = None
    height = None
    lastmove = None

    class Coin:
        player = None # 0 or 1
        color = None
        value = None

        def __init__(self, player=None, color=WHITE, value=0):
            self.player = player
            self.color = color
            assert type(value) in {float, int}, 'invalid value of coin'
            self.value = value

        def __str__(self):
            return self.color + str(self.value) + RESET


    def __init__(self, rows=8, cols=9):
        self.R = rows
        self.C = cols
        self.construct()

    def __str__(self):
        # string = REVERSE
        string += ' - '*self.C + '\n'
        for row in reversed(self.board):
            for colval in row:
                string += ' ' + str(colval) + ' '
            string += '\n'
        string += ' - '*self.C + '\n'
        string += ''.join([" {} ".format(i) for i in range(1, self.C+1)]) + '\n'
        string += ' - '*self.C + '\n'
        # string += RESET
        return string

    def construct(self):
        board = [[self.Coin() for col in range(self.C)]
                 for row in range(self.R)]
        self.board = board
        self.height = [0] * self.C

    def put(self, player=0, col=None):
        if col is None:
            raise ValueError('no column supplied')
        if self.height[col] >= self.R:
            raise RuntimeError('maximum height reached')
        self.board[self.height[col]][col] = None#TODO
        self.height[col] += 1

    def undo(self):
        if self.lastmove is None: raise
        pass

    def checkwin(self, r, c):
        pass

if __name__ == '__main__':
    b = Board()
    print(b)
