from cmd import Cmd
from color import *
from board import Board

print(RED + "colored" + CYAN + "text" + RESET)

class Game(Cmd):
    board = None

	def __init__(self, *args):
	       super().__init__()

    def do_new_game(self, arg):
        '''create a new game'''
