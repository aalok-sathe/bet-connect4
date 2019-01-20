## betConnect4
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
<!-- [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) -->

---

**betConnect4** is a command-line application in Python that lets you
play legacy Connect 4 and a modified strategy game *BetConnect4*
in your terminal!

---

### Features:
#### for the end user
- whole new strategy game involving betting on your move
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
- good example of class decoration for commandloop to help loop on
  your class while keeping names intact (not having to rename fns)
  using function annotations

### Usage:

#### installation
    $   git clone https://github.com/aalok-sathe/bet-connect4.git
    $   cd bet-connect4
    $   python3 -m pip install [--user] -r requirements.txt

#### running
    $   python3 betconnect4.py

#### gameplay instructions
##### normal connect 4
a normal game of connect 4 is played with two players taking turns to
insert coins into vertical columns of a board. a similar situation
is recreated here for you. you can play this version of the game
by specifying only the column, and not 'value' when you play (for
more instructions see below).

##### betting connect 4 [WIP]
in the proposed betting version of connect 4, there are some
additional rules.
- each coin a player inserts will have a cost to insert, _c_.
  this cost would be subtracted from the user's balance (a finite
  amount the user starts with).
- the cost of a coin, _c_, is determined by the player inserting it.
  the user may determine any cost between 1 and 10, inclusive,
  and pay the amount to insert the coin. this is the player's
  investment. why would the player want to pay to insert a coin?
- return on investment: in the event of a win, the _c_ values of the
  coins along the connected line are tallied (that means longer
  connects are better), and multiplied by a constant, **M**, the
  multiplicative factor. this sum is then extracted from the
  opponent and added to the winning player's reserve.
- in the event of a tie, the total cost of all the coins on the
  board is summed and _equally_ split among the two players. notice
  that this means the player who bet overconfidently in this round
  would lose more money relative to their opponent. however, that
  also means they have a higher incentive to go for the win
- you might think the optimal playing strategy but what if you
  made the winning condition connect 3, or maybe connect 5?

#### manual page
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
