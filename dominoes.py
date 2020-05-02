import random
from termcolor import colored, cprint

colors = {
    0: 'white',
    1: 'red',
    2: 'cyan',
    3: 'yellow',
    4: 'green',
    5: 'blue',
    6: 'magenta',
}


class Tile(object):
    def __init__(self, e1, e2):
        self.end1 = e1
        self.end2 = e2

    def print(self):
        # print tile ends with corresponding colors
        self.printEnd1()
        self.printEnd2()

    def printEnd1(self):
        cprint("[%d]" % (self.end1), colors[self.end1], sep='', end='')

    def printEnd2(self):
        cprint("[%d]" % (self.end2), colors[self.end2], sep='', end='')


class Board(object):
    def __init__(self):
        self.deck = []
        self.board = []

        # create tiles and add them to deck
        for i in range(7):
            for j in range(i, 7):
                self.deck.append(Tile(i, j))

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def distributeTiles(self):
        # create hand with 7 tiles, passes in board ends
        h1 = Hand(self.deck[0:7], self.deck[0].end1,
                  self.deck[len(self.deck) - 1].end1)

        del self.deck[0:7]  # remove hand from deck
        # self.board.append(h1.getTile()) #

    def print(self):
        for tile in self.board:
            tile.print()
        pass

    def getDeck(self):
        return self.deck


class Hand(object):
    def __init__(self, h, t1, t2):
        self.hand = h

    def isValid(self, tile):
        if t1 is None and t2 is None:
            return True

        if (tile.end1 is t1 or tile.end2 is t1
                or tile.end2 is t1 or tile.end2 is t2):
            return True

        return False

    def getTile(self):
        # if self.isValid()
        tile = self.hand[0]
        del self.hand[0]
        return tile

    def print(self):
        for tile in self.hand:
            tile.printEnd1()
            print(" ", end='')

        print()

        for tile in self.hand:
            tile.printEnd2()
            print(" ", end='')
            # for i in range(0, 7):


b = Board()
b.shuffleDeck()

playerHand
CPUHand


b.distributeTiles()

b.print()

print()
