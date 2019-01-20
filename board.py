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
    C = None
    R = None
    board = None

    def __init__(self, rows=8, cols=9):
        self.C = cols
        self.R = rows
        self.construct()

    def __str__(self):
        string = REVERSE
        string += ' - '*self.C + '\n'
        for row in reversed(self.board):
            for colval in row:
                string += ' ' + str(colval) + ' '
            string += '\n'
        string += ' - '*self.C + '\n'
        string += ''.join([" {} ".format(i) for i in range(1, self.C+1)]) + '\n'
        string += ' - '*self.C + '\n'
        string += RESET
        return string

    def construct(self):
        board = [[0 for col in range(self.C)]
                 for row in range(self.R)]
        self.board = board

b = Board()

print(b)
