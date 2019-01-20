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

        def __init__(self, player=None, value=0, color=WHITE):
            self.player = player
            if player is None:
                self.color = color
            else:
                self.color = [RED, YELLOW][player]
            assert type(value) in {float, int}, 'invalid value of coin'
            self.value = value

        def __str__(self):
            return self.color + str(self.value) + RESET

        def str_(self):
            return self.color, str(self.value)


    def __init__(self, rows=8, cols=9):
        self.R = rows
        self.C = cols
        self.construct()

    def __str__(self):
        # string = REVERSE
        off = '\t'
        # fill = ' '*5
        hsep = '-'
        vsep = '\n\n'

        string = ''
        string += off + '{:{fill}>5}'.format(hsep, fill=hsep)*(self.C+1) + '\n'

        for row in reversed(self.board):
            string += off
            for colval in row:
                col, cstr = colval.str_()
                string += '{}{:>5}{}'.format(col, cstr, RESET)
            string += vsep

        string += off + '{:{fill}>5}'.format(hsep, fill=hsep)*(self.C+1) + '\n'

        # column names
        string += off + ''.join([('{:>5}').format(i)
                                    for i in range(1, self.C+1)]) + '\n'

        string += off + '{:{fill}>5}'.format(hsep, fill=hsep)*(self.C+1) + '\n'
        # string += RESET
        return string

    def construct(self):
        board = [[self.Coin() for col in range(self.C)]
                 for row in range(self.R)]
        self.board = board
        self.height = [0] * self.C

    def put(self, player=0, col=None, value=0):
        if col is None:
            raise ValueError('no column supplied')
        if self.height[col] >= self.R:
            raise RuntimeError('maximum height reached')
        self.board[self.height[col]][col] = self.Coin(player, value)
        self.checkwin(self.height[col], col)
        self.height[col] += 1

    def undo(self):
        if self.lastmove is None: raise
        pass

    def checkwin(self, r, c, connect=4):
        for xmult in {0,1,-1}:
            for ymult in {0,1}:
                cons = 0
                for cell in range(1, connect):
                    return

if __name__ == '__main__':
    b = Board()
    print(b)
