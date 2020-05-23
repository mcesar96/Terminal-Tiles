import random
from termcolor import colored, cprint

# import sleep to show output for some time period
from time import sleep

from os import system, name


def clear():
    """Clears console window"""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


"""Global dictionary with numerical values paired with corresponding colors"""

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
    """
    An end [x] is one side of a tile with a numerical value

    Attributes:
      self.num: an integer indicating the number on an End object
    """

    def __init__(self, n):
        """Inits End object with n"""
        self.num = n

    def print(self):
        """Prints in format the value of an End"""
        if self.num is -1:        # print empty space in place of tile
            print("   ", end='')
        else:                     # print ends with corresponding colors
            cprint("[%d]" % (self.num), colors[self.num], sep='', end='')

    def __pos__(self, other):
        """overloading the addition unary operator"""
        return self.num + other.num

    def __eq__(self, other):
        """overloading the equality operator"""
        return self.num == other.num

    def __nq__(self, other):
        """overloading the inequality operator"""
        return self.num != other.num

    def __gt__(self, other):
        """overloading the greater than operator"""
        return self.num > other.num

    def __ge__(self, other):
        """overloading the greater than equality operator"""
        return self > other and self == other


class Tile(object):
    """
    A tile [x][x] is comprised of two ends

    Attributes:
      self.ptr: a pointer used to iterate over the list of Ends
      self.ends: a list of two End objects
    """

    def __init__(self, e1, e2):
        """Inits class and a list of Ends with parameter integers"""
        self.ptr = 0
        self.ends = [End(e1), End(e2)]

    def getEnd1(self):
        return self.ends[0]

    def getEnd2(self):
        return self.ends[1]

    def flip(self):
        """Swaps the placement of End1 and End2 in end list"""
        self.ends[0], self.ends[1] = self.ends[1], self.ends[0]

    def isDouble(self):
        """Returns true if ends are equivalent"""
        return self.ends[0] == self.ends[1]

    def print(self):
        """Calls each End object's print function"""
        for e in self.ends:
            e.print()

    def __eq__(self, other):
        """overloading the equality operator"""
        return (self.ends[0] == other.ends[0]) and (self.ends[1] == other.ends[1])

    def __gt__(self, other):
        """overloading the greater than operator"""
        return self.ends[0].num + self.ends[1].num > other.ends[0].num + other.ends[1].num
        pass

    def __iter__(self):
        """returns an iter (object with a "next" function)"""
        self.ptr = 0
        return self

    def __next__(self):
        """the iterator returns the next value"""
        if self.ptr == len(self.ends):  # list ptr has reached end of list
            raise StopIteration

        s = self.ends[self.ptr]
        self.ptr += 1

        return s


class Deck(object):
    """
    A deck [x][x] [x][x] [x][x] is a list comprised of 28 tiles to be distributed to hands

    Attributes:
      self.deck: a list of Tile objects
      self.size: a variable used to initialize the deck
    """

    def __init__(self):
        """Initialize variables"""
        self.deck = []
        self.size = 7

        # create tiles and add them to deck
        for i in range(self.size):
            for j in range(i, self.size):
                self.deck.append(Tile(i, j))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        """Returns a tile object from deck"""
        if self.deck:
            return self.deck.pop()

    def getHand(self):
        """Returns a hand object with tiles from deck"""
        if not self.deck:  # if the deck is empty
            raise Exception("All tiles have been distributed")

        tiles = []

        # takes tiles from deck and place in hand
        for i in range(self.size):
            tiles.append(self.deck.pop())

        return Hand(tiles)


class Hand(object):
    """
    A hand [x][x] [x][x] [x][x] is a list comprised of 7 tiles from the deck

    Attributes:
      self.hand: a list of Tile objects
    """

    def __init__(self, l=[]):
        self.hand = l

    def getHighestDouble(self):
        tile = Tile(-1, -1)

        # get first double
        for t in self.hand:
            if t.isDouble():
                tile = t

        # find highest double
        for t in self.hand:
            if t.isDouble() and t.getEnd1() > tile.getEnd1():
                tile = t

        return tile

    def print(self):
        print("---------------------------")

        for t in self.hand:
            t.getEnd1().print()
            print(" ", end='')

        print()

        for t in self.hand:
            t.getEnd2().print()
            print(" ", end='')

        print("\n ", end='')

        i = 0
        for t in self.hand:
            print(i, "  ", end='')
            i += 1

        print()


class Board(object):
    """
    A board is comprised of a tile matrix, a list, a deck, and two hands
    The list of tiles keeps track of all tiles placed by players

    Attributes:
      self.deck: a shuffled deck object
      self.bool: a bool that determines if starting tile has been placed
      self.size: the size of the board (2D matrix)
      self.board: game board that's printed to console
      self.lhs_row, self.lhs_col: coordinates of left most tile on board
      self.rhs_row, self.rhs_col: coordinates of right most tile on board
    """

    def __init__(self):
        """Initialize variables and create board"""
        self.deck = Deck()
        self.deck.shuffle()

        self.is_first_double = False

        self.size = 30

        # create board matrix of size x size
        self.board = [[Tile(-1, -1) for x in range(self.size)]
                      for y in range(self.size)]

        self.mid_point = int(self.size / 2)

        # respective tile positions
        self.lhs_row, self.lhs_col = self.mid_point, self.mid_point
        self.rhs_row, self.rhs_col = self.mid_point, self.mid_point

    def isValid(self, h, i):
        """Returns true if tile can be placed on board"""
        tile = h[i]  # get tile from player's hand
        # get the ends of the left and right hand board pieces
        lhs = self.board[self.lhs_row][self.lhs_col].getEnd1()
        rhs = self.board[self.rhs_row][self.rhs_col].getEnd2()

        if lhs == tile.getEnd1():
            return True
        elif lhs == tile.getEnd2():
            return True
        elif rhs == tile.getEnd1():
            return True
        elif rhs == tile.getEnd2():
            return True

        return False

    def placeHighestDouble(self, h1):
        i = 0
        for t in h1.hand:
            if t == h1.getHighestDouble():
                self.board[self.mid_point][self.mid_point] = t
                del h1.hand[i]
                return
            i += 1

    def placeTile(self, t, side, row, col):
        """Initiazes board coordinate with tile, returns updated coordinate"""
        if side is 'l':
            # if the tile ends don't match up by default, swap the values
            if self.board[row][col].getEnd1() == t.getEnd1():
                t.flip()

            col -= 1

        elif side is 'r':
            # if the tile ends don't match up by default, swap the values
            if self.board[row][col].getEnd2() != t.getEnd1():
                t.flip()

            col += 1

        self.board[row][col] = t  # place tile on board with new coordinate
        return col                # return updated coordinate

    def place(self, h, i):
        """Logic for determining where to place tile on board and updating user hand"""
        tile = h[i]  # get tile from player's hand

        # get the ends of the left and right hand board pieces
        lhs = self.board[self.lhs_row][self.lhs_col].getEnd1()
        rhs = self.board[self.rhs_row][self.rhs_col].getEnd2()

        # placement on left hand side
        if lhs == tile.getEnd1() or lhs == tile.getEnd2():

            # possible placement on both left hand and right hand side
            if rhs == tile.getEnd1() or rhs == tile.getEnd2():
                side = input("Enter side (l/r): ")

                if side is 'r':
                    self.rhs_col = self.placeTile(
                        tile, 'r', self.rhs_row, self.rhs_col)

                    del h[i]        # delete index from hand
                    return Hand(h)  # return updated hand object

            self.lhs_col = self.placeTile(
                tile, 'l', self.lhs_row, self.lhs_col)

            del h[i]        # delete index from hand
            return Hand(h)  # return updated hand object

        # placement on right hand side
        elif rhs == tile.getEnd1() or rhs == tile.getEnd2():
            self.rhs_col = self.placeTile(
                tile, 'r', self.rhs_row, self.rhs_col)

            del h[i]        # delete index from hand
            return Hand(h)  # return updated hand object

        else:
            # change this to draw function later
            print("Invalid tile placement.")
            sleep(1)
            return Hand(h)  # return hand unupdated

    def print(self):
        for row in self.board:
            for col in row:
                col.print()
            print()


def main():
    b = Board()
    player = b.deck.getHand()
    cpu = b.deck.getHand()
    is_player_turn = True
    i = 0

    clear()
    b.print()
    print("Player\n")
    player.print()
    print('\n')

    sleep(4)

    if player.getHighestDouble() > cpu.getHighestDouble():
        b.placeHighestDouble(player)
        is_player_turn = True
    elif cpu.getHighestDouble() > player.getHighestDouble():
        b.placeHighestDouble(cpu)
    else:
        b.placeHighestDouble(cpu)

    while True:
        clear()
        b.print()
        print("Player\n")
        player.print()
        print('\n')

        if is_player_turn:
            while True:
                i = 0

                while not b.isValid(player.hand, i):
                    i += 1

                clear()
                b.print()
                player.print()
                sleep(1)

                index = input("\nEnter tile: ")
                player = b.place(player.hand, int(index))


if __name__ == '__main__':
    main()
