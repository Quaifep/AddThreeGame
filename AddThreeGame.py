# Author: Paul Quaife
# Date: 2/23/2021
# Description: Plays a game that allows two players to play a game in which they alternately choose numbers from 1-9.

def __init__(self):
    """initial def that assigns players."""
    self.__p1 = 0
    self.__p2 = 0
    self.__played = []
    self.__str = "UNFINISHED"

def get_current_state(self):
    """returns current state of game"""
    return self.__str

def make_move(self, pl, x):
    """def that controls when player makes a move."""
    if x in self.__played:
        return False
    if x > 9 or x < 1:
        return False
    if pl == "first":
        self.__pl = self.__p1 + x
        self.__played.append(x)
    elif pl == "second":
        self.__p2 = self.__p2 + x
        self.__played.append(x)
    if self.__p1 == 15 and self.__p2 == 15:
        self.__str = "DRAW"
    elif self.__p1 == 15:
        self.__str = "FIRST_WON"
    elif self.__p2 == 15:
        self.__str = "SECOND_WON"
    if len(self.__played) == 9:
        self.__str = "DRAW"
    return True

    while True:
        x = int(input("Player 1 please enter a number: "))
    while True:
        if game.make_move("first", x) == True:
            else x = int(input("Invalid input! Player 2 please re-enter a number: "))

state = game.get_current_state()
    if state == "UNFINISHED":
        print("No one reached 15. Get ready for next round.")
    elif state == "FIRST_WON":
        print("First player won!!!")
    elif state == "SECOND_WON":
        print("Second player won!!!")
    elif state == "DRAW":
        print("Game ends in draw")

