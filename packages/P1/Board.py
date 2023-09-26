import random
import copy

class Board:
    directions = ["right", "left", "down", "up"]

    @staticmethod
    def fromString(string: str):
        return Board(Board.parseString(string))

    @staticmethod
    def parseString(string: str):
        vals = list(int(s) for s in list(string) if s != " ")
        split = Board.parseList(vals)
        return list(split)

    @staticmethod
    def parseList(ls: list):
        return [ls[i:i+3] for i in range(0, len(ls), 3)]

    @staticmethod
    def fromList(ls: list):
        return Board(Board.parseList(ls))

    @staticmethod
    def randomState(n:int = 1000):
        r = Board()
        [r.move(Board.directions[i]) for i in [random.randint(0, 3) for j in range(n)]]
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
        return [i for i in [[(i, j) for j in range(len(self.value[i])) if self.value[i][j] == a] for i in range(len(self.value))] if len(i) > 0][0][0]

    def updateZero(self):
        self.zero = self.findValue(0)

    def printState(self):
        print(str(self))

    def setState(self, string: str):
        self.value = self.parseString(string)
        self.updateZero()

    def randomizeState(self, n=1000):
        rs = Board.randomState(n)
        self.value = rs.value
        self.zero = rs.zero

    def move(self, direction: str):
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
