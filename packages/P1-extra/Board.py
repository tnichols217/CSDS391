import random
import copy

class Board:
    directions = ["right", "left", "down", "up"]

    @staticmethod
    def fromString(string: str):
        """Constructs a new Board from a string"""
        return Board(Board.parseString(string))

    @staticmethod
    def parseString(string: str):
        """Parses an input string into a useable list for creating a Board"""
        vals = list(int(s) for s in list(string) if s != " ")
        split = Board.parseList(vals)
        return list(split)

    @staticmethod
    def parseList(ls: list):
        """Parses a flat list into a 2D array"""
        return [ls[i:i+3] for i in range(0, len(ls), 3)]

    @staticmethod
    def fromList(ls: list):
        """Constructs a new Board from a flat list"""
        return Board(Board.parseList(ls))

    @staticmethod
    def randomState(n:int = 1000, seed:int = 12497989):
        """Constructs a random Board"""
        R = random.Random(seed)
        r = Board()
        [r.move(Board.directions[i]) for i in [R.randint(0, 3) for j in range(n)]]
        return r

    def __init__(self, value=[[0,1,2],[3,4,5],[6,7,8]]):
        self.value = copy.deepcopy(value)
        self.updateZero()

    def __str__(self):
        string = "\n".join(("".join(str(j) for j in i) for i in self.value))
        return string

    def __repr__(self):
        string = " ".join(("".join(str(j) for j in i) for i in self.value))
        return string

    def __copy__(self):
        return Board(self.value)

    def findValue(self, a):
        """Gives the coordinates of a value in the Board"""
        return [i for i in [[(i, j) for j in range(len(self.value[i])) if self.value[i][j] == a] for i in range(len(self.value))] if len(i) > 0][0][0]

    def updateZero(self):
        """Updates the zero location in order to speed up game moves"""
        self.zero = self.findValue(0)

    def printState(self):
        """Print state to stdout"""
        print(str(self))

    def setState(self, string: str):
        """Updates state and zero location"""
        self.value = self.parseString(string)
        self.updateZero()

    def randomizeState(self, n=1000, seed:int = 12497989):
        """Generates a randomized Board then sets it to this object"""
        rs = Board.randomState(n, seed)
        self.value = rs.value
        self.zero = rs.zero

    def move(self, direction: str):
        """Moves a piece in a particular direction if possible"""
        if direction == Board.directions[0] and self.zero[1] > 0:
            self.value[self.zero[0]][self.zero[1]], self.value[self.zero[0]][self.zero[1]-1] = (self.value[self.zero[0]][self.zero[1]-1], self.value[self.zero[0]][self.zero[1]])
            self.zero = (self.zero[0], self.zero[1]-1)
        elif direction == Board.directions[1] and self.zero[1] < len(self.value[self.zero[0]]) - 1:
            self.value[self.zero[0]][self.zero[1]], self.value[self.zero[0]][self.zero[1]+1] = (self.value[self.zero[0]][self.zero[1]+1], self.value[self.zero[0]][self.zero[1]])
            self.zero = (self.zero[0], self.zero[1]+1)
        elif direction == Board.directions[2] and self.zero[0] > 0:
            self.value[self.zero[0]][self.zero[1]], self.value[self.zero[0]-1][self.zero[1]] = (self.value[self.zero[0]-1][self.zero[1]], self.value[self.zero[0]][self.zero[1]])
            self.zero = (self.zero[0]-1, self.zero[1])
        elif direction == Board.directions[3] and self.zero[0] < len(self.value) - 1:
            self.value[self.zero[0]][self.zero[1]], self.value[self.zero[0]+1][self.zero[1]] = (self.value[self.zero[0]+1][self.zero[1]], self.value[self.zero[0]][self.zero[1]])
            self.zero = (self.zero[0]+1, self.zero[1])
