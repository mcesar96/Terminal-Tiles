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


class End(object):
    def __init__(self, e):
        self.num = int(e)

    def print(self):
        # print ends with corresponding colors
        cprint("[%d]" % (self.num), colors[self.num], sep='', end='')

    def __eq__(self, other):
        # overloading the equals operator
        return self.num is other.num

    def __nq__(self, other):
        # overloading the not equals operator
        return not self == other


class Tile(object):
    def __init__(self, e1, e2):
        self.end1 = e1
        self.end2 = e2

    def print(self):
        self.end1.print()
        self.end2.print()

    def __eq__(self, other):
        # overloading the equals operator
        return self.end1 == other.end1 and self.end2 == other.end2

    def __nq__(self, other):
        # overloading the not equals operator
        return not self == other


class TileList(object):
    def __init__(self, l=[]):
        self.list = l

    def getList(self):
        return self.list

    def isEmpty(self):
        return not self.list

    def print(self):
        for t in self.list:
            t.end1.print()
            print(" ", end='')

        print()

        for t in self.list:
            t.end2.print()
            print(" ", end='')


class Deck(TileList):
    def __init__(self):
        super().__init__()

        # create tiles and add them to deck
        for i in range(7):
            for j in range(i, 7):
                t = Tile(End(i), End(j))
                self.list.append(t)

    def shuffle(self):
        random.shuffle(self.list)

    def distributeHand(self):
        if self.isEmpty():
            raise Exception("All tiles have been distributed")

        hand = Hand()

        # takes tiles from deck and place in hand
        for i in range(7):
            hand.list.append(self.list.pop())

        return hand

    def print(self):
        # this overrides the TileList print function
        print()


class Hand(TileList):
    def __init__(self):
        super().__init__()
        self.list = []
        pass
