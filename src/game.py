import random

class Game:

    def __init__(self):
        self._isStart = False
        self._isOver = False
        self._lstPlayer = []
        self._lstAvailableChoice = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        self._dictIndexToButtonName = { 1: "btn1", 2: "btn2", 3: "btn3", 4: "btn4", 5: "btn5", 6: "btn6", 7: "btn7", 8: "btn8", 9: "btn9" }


    @property
    def isStart(self):
        return self._isStart

    @property
    def isOver(self):
        return self._isOver

    @property
    def lstPlayer(self):
        return self._lstPlayer
     
    @property
    def lstAvailableChoice(self):
        return self._lstAvailableChoice

    @property
    def dictIndexToButtonName(self):
        return self._dictIndexToButtonName


    def add_player(self, lstPlayer):
        
        for player in lstPlayer:
            self._lstPlayer.append(player)


    def is_all_in(self, lstExpect, lstNum):

        isAllIn = True

        for number in lstExpect:
            isNumberInList = number in lstNum

            if (not isNumberInList):
                isAllIn = False
                break

        return isAllIn


    def check_winner(self):

        for player in self._lstPlayer:

            if (self.is_all_in( [ 1, 2, 3 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 4, 5, 6 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 7, 8, 9 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 1, 4, 7 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 2, 5, 8 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 3, 6, 9 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 1, 5, 9 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 3, 5, 7 ], player.lstSelectedNum )):
                player.win()


    def start(self):
        self._isStart = True


    def over(self):
        self._isOver = True


class Player:

    def __init__(self, name, marking):
        self._name = name
        self._marking = marking
        self._isWin = False
        self._isTurn = False
        self._lstSelectedNum = []

    @property
    def name(self):
        return self._name

    @property
    def marking(self):
        return self._marking

    @property
    def isWin(self):
        return self._isWin

    @property
    def isTurn(self):
        return self._isTurn

    @property
    def lstSelectedNum(self):
        return self._lstSelectedNum


    @marking.setter
    def marking(self, value):
        self._marking = value

    @isWin.setter
    def isWin(self, value):
        self._isWin = value

    @isTurn.setter
    def isTurn(self, value):
        self._isTurn = value


    def start_first(self):
        self._isTurn = True

    def win(self):
        self._isWin = True

    def lose(self):
        self._isWin = False 


class Bot(Player):

    def random_pick(self, lstNum):

        randomNum = 0

        if (len(lstNum) > 0):
            index = random.randint(0, len(lstNum) - 1)
            randomNum = lstNum[index]

        return randomNum