from sys import stdout, stderr
from cmd import Cmd
from color import *
from board import Board
from art import tprint
import random
import inspect
import types

LICENSE = '''
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
    For usage instructions, type 'help' or '?'
    '''
    board = None
    turn = None
    STARTMONEY = float('inf')
    winreq = 4

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
            if col == -1: col = None
            if len(spl) == 2:
                val = spl[1]
            win, best = self.board.put(player=self.turn, col=col, value=val,
                                       wincondition=self.winreq)
            if win:
                print(REVERSE, [RED, YELLOW][self.turn],
                      '{o:>{w}}'.format(o='', w=80), RESET, file=stderr)
                tprint('player  {}\nhas won!\n{} in a row'.format(self.turn,
                                                                  best))
                print(REVERSE, [RED, YELLOW][self.turn],
                      '{o:>{w}}\n'.format(o='', w=80), RESET, file=stderr)
                self.exit(None)

            self.turn = (self.turn + 1) % 2
            self.status()
        except (ValueError, IndexError):
            err()
            print('bad column index', file=stderr)
        except RuntimeError:
            err()
            print('maximum height in column reached', file=stderr)

    def reset(self, arg=None) -> 'loop':
        resp = input('reset current game? [y]/n')
        if resp in {'', 'y', 'Y', 'yes', 'ye'}:
            self.newgame()
        return

    def wincondition(self, arg=None) -> 'loop':
        if not arg:
            print(self.winreq)
        else:
            try:
                x = int(arg)
                self.winreq = x
            except ValueError:
                err()
                print('bad argument to wincondition', file=stderr)

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
        {bold}newgame [ROW COL]{reset}:
            initiates a game of bet-connect4

            [ROW COL]: makes the board dimensions row, col


        {bold}wincondition [NUM]{reset}:
            gets the winning condition.

            [NUM]: set the winning condition to NUM. default is 4 ('connect 4'),
                   so using this command would set the winning condition
                   to something else.


        {bold}status{reset}:
            shows current game board and status
            including players, their money, and who goes next


        {bold}[play] COL [VALUE]{reset}:
            plays the next turn

            COL (required): column number to play coin in
            [VALUE]: amount to bet on this coin location


        {bold}reset{reset}:
            resets the current game progress and starts over


        {bold}exit|quit|q|close{reset}:
            exits the program

        '''.format(bold=BOLD, reset=RESET)
        print(help)

    def license(self, arg=None) -> 'loop':
        '''shows license text'''
        print(LICENSE)

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
