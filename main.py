from sys import stdout, stderr
from cmd import Cmd
from color import *
from board import Board
from art import tprint

def err():
    print(RED + 'ERR: ' + RESET, file=stderr, end='')
def info():
    print(YELLOW + 'ERR: ' + RESET, file=stderr, end='')

print("welcome to\n" + BOLD + "bet" + RED + "connect" + GREEN + "4" + RESET)
tprint("bet connect 4", font='bell')

class Game(Cmd):
    board = None

    def __init__(self, *args):
        super().__init__()

    def do_new_game(self, arg):
        '''create a new game.
        usage: new_game [rows cols]
        default value: new_game [8 9]
        '''
        if len(arg):
            try:
                r, c = (int(x) for x in arg.split())
                self.board = Board(r, c)
            except ValueError:
                err()
                print('usage: `new_game [rows cols]`', file=stderr)
        else:
            self.board = Board()


    def do_help(self, arg):
        '''show helpful usage message'''
        pass

    def do_exit(self, arg):
        '''exit program'''
        raise SystemExit

if __name__ == '__main__':
    prompt = Game("")
    prompt.prompt = '>> '
    try:
    	prompt.cmdloop('''
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See the GNU GPL v3.
    For usage instructions, type "help"''')
    except KeyboardInterrupt :
    	print("\nExiting due to KeyboardInterrupt")
    	raise SystemExit
