# Author: Paul Quaife
# Date: 3/1/2021
# Description: Plays a game that allows two players to play a game in which they alternately choose numbers from 1-9.

class AddThreeGame:
    pass

    def __init__(self):
        """initial def that assigns players."""
        self.__p1 = 0
        self.__p2 = 0
        self.__played = []
        self.__str = "UNFINISHED"

    def get_current_state(self):
        """returns current state of game"""
        game = AddThreeGame()
        state = game.get_current_state()

        if state == "UNFINISHED":
            return True
        elif state == "FIRST_WON":
            return True
        elif state == "SECOND_WON":
            return True
        elif state == "DRAW":
            return True

        return self.__str

    def make_move(self, pl, x):
        """def that controls when player makes a move."""
        if x in self.__played:
            return False
        if x > 9 or x < 1:
            return False
        if pl == "first":
            self.__p1 = self.__p1 + x
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
