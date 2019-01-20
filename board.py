"""
convention: bottom row first
"""
from color import *
from sys import stdout, stderr

def err():
    print(RED + 'ERR: ' + RESET, file=stderr, end='')
def info():
    print(YELLOW + 'INFO: ' + RESET, file=stderr, end='')


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

    def put(self, player=None, col=None, value=0, wincondition=4):
        if col is None:
            raise ValueError('no column supplied')
        if self.height[col] >= self.R:
            raise RuntimeError('maximum height reached')
        self.board[self.height[col]][col] = self.Coin(player, value)
        win = self.checkwin(self.height[col], col, wincondition)
        self.height[col] += 1
        return win

    def undo(self):
        raise NotImplementedError('not yet implemented')
        if self.lastmove is None: raise
        pass

    def checkwin(self, r, c, connect=4):
        this_coin = self.board[r][c]
        info()
        print('inserted at height: {}, col: {}'.format(r+1, c+1), file=stderr)
        info()
        print('conducting win checks with win condition {}'.format(connect),
              file=stderr)
        bestconsec = 1
        for xmult in {0,1,-1}:
            for ymult in {0,1}:
                if xmult == ymult == 0: continue
                consec = 1
                for dist in range(1, connect):
                    if r+ymult*dist <=0 or c+xmult*dist <= 0: continue
                    try:
                        o_coin = self.board[r+ymult*dist][c+xmult*dist]
                        if o_coin.player is None: break
                        if this_coin.player == o_coin.player:
                            consec += 1
                        else:
                            break
                    except IndexError:
                        break
                for dist in range(1, connect):
                    dist *= -1
                    try:
                        o_coin = self.board[r+ymult*dist][c+xmult*dist]
                        if o_coin.player is None: break
                        if this_coin.player == o_coin.player:
                            consec += 1
                        else:
                            break
                    except IndexError:
                        break
                info()
                print('coin: {}, xmult: {}, '
                      'ymult: {}, consec: {}'.format(this_coin, xmult, ymult,
                                                     consec), file=stderr)
                bestconsec = max(bestconsec, consec)
        if bestconsec >= connect: return True, bestconsec#, xmult, ymult, consec
        return False, 0

if __name__ == '__main__':
    b = Board()
    print(b)
