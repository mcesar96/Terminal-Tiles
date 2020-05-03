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


# t = Tile(End(1), End(2))
# t2 = Tile(End(1), End(2))

# if t == t2:
#     t.print()

class TileList(object):
    def __init__(self):
        self.list = []

    def setList(self, l):
        self.list = l

    def append(self, t):
        self.list.append(t)

    def getList(self):
        return self.list

    def remove(self, t):
        self.list.remove(t)

    def isEmpty(self):
        return not self.list

    def print(self):
        for t in self.list:
            t.print()


class Deck(TileList):
    def __init__(self):
        super().__init__()

        # create tiles and add them to deck
        for i in range(7):
            for j in range(i, 7):
                self.list.append(Tile(End(i), End(j)))

    def shuffle(self):
        random.shuffle(self.list)


d = Deck()
d.print()
# class Board(object):
#     def __init__(self):
#         self.deck = []
#         self.board = []

#         # create tiles and add them to deck
#         for i in range(7):
#             for j in range(i, 7):
#                 self.deck.append(Tile(i, j))

#     def shuffleDeck(self):
#         random.shuffle(self.deck)

#     def getHand(self):
#         if not self.deck:
#             raise Exception("All tiles have been distributed")

#         # create hand with 7 tiles, passes in board ends
#         hand = Hand(self.deck[0:7], self.deck[0].end1,
#                     self.deck[len(self.deck) - 1].end1)

#         del self.deck[0:7]  # remove hand from deck
#         return hand

#         # self.board.append(h1.getTile()) #

#     def print(self):
#         for tile in self.board:
#             tile.print()

#     def getDeck(self):
#         return self.deck

#     def getBoard(self):
#         return self.board


# class Hand(object):
#     def __init__(self, h, t1, t2):
#         self.hand = h
#         self.boardEnd1 = t1
#         self.boardEnd2 = t2

#     def isValid(self, tile):
#         # if the board is empty
#         if not self.boardEnd1:
#             return True

#         if (tile.end1 is t1 or tile.end2 is t1
#                 or tile.end1 is t2 or tile.end2 is t2):
#             return True

#         # if ntile.end1 is t1 or tile.end2 is t1
#         #     or tile.end2 is t1 or tile.end2 is t2):
#         #     return True

#         return False

#     def placeTile(self, t):
#         if t not in self.hand:
#             print("That tile is not in your hand.\n")
#             return

#         if not self.isValid(t):
#             print("That tile can not be placed on the board.\n")
#             return

#         for tile in self.hand:
#             if tile == t:
#                 self.hand.remove(tile)
#                 return t

#     def print(self):
#         for tile in self.hand:
#             tile.printEnd1()
#             print(" ", end='')

#         print()

#         for tile in self.hand:
#             tile.printEnd2()
#             print(" ", end='')
#             # for i in range(0, 7):


# b = Board()
# # b.shuffleDeck()

# playerHand = b.getHand()
# computerHand = b.getHand()

# tile = Tile(0, 0)
# playerHand.placeTile(tile)

# print("Player: \n")
# playerHand.print()

# print("\n\n")
# b.print()

# e = End(1)
# print(end)
# # print("CPU: \n")
# # computerHand.print()


# # b.print()

print()
