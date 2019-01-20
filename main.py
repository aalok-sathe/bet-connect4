from sys import stdout, stderr
from cmd import Cmd
from color import *
from board import Board
from art import tprint
import random
import inspect
import types

def err():
    print(RED + 'ERR: ' + RESET, file=stderr, end='')
def info():
    print(YELLOW + 'INFO: ' + RESET, file=stderr, end='')

# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

print("welcome to\n" + BOLD + "bet" + RED + "connect" + GREEN + "4" + RESET)
tprint("bet connect 4", font='bell')

def mklooped(cls):
    for name, ob in inspect.getmembers(cls):
        if not type(ob) is types.FunctionType: continue
        if getattr(ob, '__annotations__').get('return', None) == 'loop':
            setattr(cls, 'do_' + ob.__name__, ob)
    return cls


@mklooped
class Game(Cmd):
    intro = '''
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See the GNU GPL v3.
    For usage instructions, type "help"
    '''
    board = None
    turn = None
    STARTMONEY = float('inf')

    class Player:
        money = None
        num = None

        def __init__(self, num=None, money=0):
            if num is not None:
                self.num = num
            else:
                raise ValueError('playernum cannot be `None`')
            self.money = money

        def __str__(self):
            blurb = 'player{num}'.format(num=self.num)
            money = 'remaining money: {mon}'.format(mon=self.money)
            text = '{:>20} {:>40}'.format(blurb, money)
            return [RED, YELLOW][self.num] + text + RESET

        def placebet(self, value):
            if value <= self.money:
                self.money -= value
                return value
            return 0

    def __init__(self, *args):
        super().__init__()

    # def do_config(self, arg):
    #     '''set config values
    #     usage:
    #     '''


    def newgame(self, arg=None) -> 'loop':
        '''create a new game.
        usage: new_game [rows cols]
        default value: new_game [8 9]
        '''
        if arg is not None and len(arg):
            try:
                r, c = (int(x) for x in arg.split())
                self.board = Board(r, c)
            except ValueError:
                err()
                print('usage: `new_game [rows cols]`', file=stderr)
        else:
            self.board = Board()
        self.players = [self.Player(0, self.STARTMONEY),
                        self.Player(1, self.STARTMONEY)]
        self.turn = random.randint(0,1)

        self.status()

    def status(self, arg=None) -> 'loop':
        '''show the current game status'''
        if self.board is None:
            err()
            print('need to create a new game first', file=stderr)
        else:
            playerstats = [str(p) for p in self.players]
            print(self.board)
            if self.turn == 0:
                print(REVERSE, end='')
            print(playerstats[0])
            if self.turn == 1:
                print(REVERSE, end='')
            print(playerstats[1])

    def play(self, arg=None) -> 'loop':
        '''play the next turn'''
        if self.board is None:
            err()
            print('need to create a new game first', file=stderr)
            return
        try:
            spl = [int(x) for x in arg.split()]
            col, val = spl[0]-1, 0
            if len(spl) == 2:
                val = spl[1]
            win = self.board.put(player=self.turn, col=col, value=val)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1e36cc9902d4618851c916c5091cd46d98c41792
            if win:
                tprint('player {} has won!'.format(self.turn))
                print(REVERSE, [RED, YELLOW][self.turn],
                      '{:>{w}}'.format(w=80), RESET)
                raise SystemExit
<<<<<<< HEAD
=======
=======
            print(win)
>>>>>>> 09ded09e4ff81429bae403a28ca8bc0afdf058e2
>>>>>>> 1e36cc9902d4618851c916c5091cd46d98c41792
            self.turn = (self.turn + 1) % 2
            self.status()
        except (ValueError, IndexError):
            err()
            print('need to specify a proper column number that\'s an integer',
                  file=stderr)
        except RuntimeError:
            err()
            print('maximum height in column reached', file=stderr)

    def reset(self, arg=None) -> 'loop':
        resp = input('reset current game? [y]/n')
        if resp in {'', 'y', 'Y', 'yes', 'ye'}:
            self.newgame()
        return

    def emptyline(self):
        '''what to do with an empty prompt'''
        if self.board is not None:
            self.status(None)

    def default(self, line):
        # print(repr(line))
        if line in {'quit', 'q', 'exit', 'close'}:
            self.exit(line)
        try:
            _ = [int(x) for x in line.split()]
            self.play(line)
        except ValueError:
            super().default(line)

    def help(self, arg=None) -> 'loop':
        '''show helpful usage message'''
        help = '''
        {bold}newgame [row col]{reset}:
            initiates a game of bet-connect4

            [row col]: makes the board dimensions row, col


        {bold}status{reset}:
            shows current game board and status
            including players, their money, and who goes next


        {bold}[play] col [value]{reset}:
            plays the next turn

            col (required): column number to play coin in
            [value]: amount to bet on this coin location


        {bold}reset{reset}:
            resets the current game progress and starts over

        {bold}exit|quit|q|close{reset}:
            exits the program

        '''.format(bold=BOLD, reset=RESET)
        print(help)

    def exit(self, arg=None) -> 'loop':
        '''exit program'''
        raise SystemExit

if __name__ == '__main__':
    prompt = Game("")
    prompt.prompt = '(betconnect4)$ '
    try:
    	prompt.cmdloop()
    except KeyboardInterrupt :
    	print("\nExiting due to KeyboardInterrupt")
    	raise SystemExit
