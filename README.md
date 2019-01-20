## pyConnect4
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

---
**pyConnect4** is a command-line application in Python that lets you play connect 4 in your terminal!

### Features:
#### for the end user
- construct a board of any size (rows, columns)
- multiplayer mode
- colored output
- live track of who plays next
- tells you when you win
- manually set win condition (connect4? connect5? connect32?)
- nice ascii art to boost your spirits

#### for the hacker
- decent API functions:
    - `board.py`: functions related to constructing a board, managing
    coin-spawning on the board, checking for victory in an existing
    board, adding an associated 'value' to each coin, and so on
    - `connect4.py`: a nice implementation of a command-loop game
    process making use of `board.py`, a `player` class

### Usage:

#### installation
    $   git clone https://github.com/aalok-sathe/bet-connect4.git
    $   cd bet-connect4

#### running
    $   python3 connect4.py
---
    >   help

        newgame [ROW COL]:
        initiates a game of bet-connect4

            [ROW COL]: makes the board dimensions row, col


        wincondition [NUM]:
            gets the winning condition.

            [NUM]: set the winning condition to NUM. default is 4 ('connect 4'),
                   so using this command would set the winning condition
                   to something else.


        status:
            shows current game board and status
            including players, their money, and who goes next


        [play] COL [VALUE]:
            plays the next turn

            COL (required): column number to play coin in
            [VALUE]: amount to bet on this coin location


        reset:
            resets the current game progress and starts over


        exit|quit|q|close:
            exits the program
