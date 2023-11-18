import random
import copy

class Rubiks:
    directions = [
        "U",
        "U2",
        "U'",
        "D",
        "D2",
        "D'",
        "L",
        "L2",
        "L'",
        "R",
        "R2",
        "R'",
        "F",
        "F2",
        "F'",
        "B",
        "B2",
        "B'"
    ]
    colors = ["W", "G", "R", "B", "O", "Y"]

    @staticmethod
    def fromString(string: str):
        """Constructs a new Rubiks from a string"""
        return Rubiks(Rubiks.parseString(string))

    @staticmethod
    def parseString(string: str):
        """Parses an input string into a useable list for creating a Rubiks"""
        chars = list(s for s in list(string) if s != " ")
        vals = list([int(chars[i], int(chars[i+1]))] for i in range(0, len(chars), 2))
        split = Rubiks.parseList(vals)
        return list(split)

    @staticmethod
    def parseList(ls: list):
        """Parses a the input array"""
        return [[i for i in j] for j in ls]

    @staticmethod
    def fromList(ls: list):
        """Constructs a new Rubiks from a flat list"""
        return Rubiks(Rubiks.parseList(ls))

    @staticmethod
    def randomState(n:int = 1000, seed:int = 12497989):
        """Constructs a random Rubiks"""
        R = random.Random(seed)
        r = Rubiks()
        [r.move(Rubiks.directions[i]) for i in [R.randint(0, len(Rubiks.directions)-1) for _ in range(n)]]
        return r

    '''
    WGR
    WRB
    WBO
    WOG
    YGO
    YOB
    YBR
    YRG
    '''

    @staticmethod
    def getColors(n:int, r:int = 0):
        """Returns an ordered list of colors for a given piece number"""
        N = 7 - n if n >= 4 else n
        o = [Rubiks.colors[0 if n < 4 else 5], Rubiks.colors[(N + (n>=4)) %4 +1], Rubiks.colors[(N + (n<4)) %4 +1]]
        return [o[(i+r)%3] for i in range(3)]

    def __init__(self, value=[[0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0]]):
        self.value = copy.deepcopy(value)

    '''
      WW
      WW
    GGRRBBOO
    GGRRBBOO
      YY
      YY

      32
      01
    30011223
    47766554
      76
      45

      00
      00
    21212121
    12121212
      00
      00
    '''

    def __str__(self):
        c = [Rubiks.getColors(i[0], i[1]) for i in self.value]
        string = f"  {c[3][0]}{c[2][0]}"
        string += f"\n  {c[0][0]}{c[1][0]}"
        string += f"\n{c[3][2]}{c[0][1]}{c[0][2]}{c[1][1]}{c[1][2]}{c[2][1]}{c[2][2]}{c[3][1]}"
        string += f"\n{c[4][1]}{c[7][2]}{c[7][1]}{c[6][2]}{c[6][1]}{c[5][2]}{c[5][1]}{c[4][2]}"
        string += f"\n  {c[7][0]}{c[6][0]}"
        string += f"\n  {c[4][0]}{c[5][0]}"
        return string

    def __repr__(self):
        string = " ".join(("".join(str(j) for j in i) for i in self.value))
        return string

    def __copy__(self):
        return Rubiks(self.value)

    def printState(self):
        """Print state to stdout"""
        print(str(self))

    def setState(self, string: str):
        """Updates state and zero location"""
        self.value = self.parseString(string)

    def randomizeState(self, n=1000, seed:int = 12497989):
        """Generates a randomized Rubiks then sets it to this object"""
        rs = Rubiks.randomState(n, seed)
        self.value = rs.value

    def move(self, direction: str):
        """Moves a piece in a particular direction if possible"""
        d = Rubiks.directions.index(direction)
        g = d // 3
        p = d % 3
        # Counter clockwise cuboid numbers per face, by move group order
        Vs = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 3, 4, 7],
            [2, 1, 6, 5],
            [1, 0, 7, 6],
            [3, 2, 5, 4]
        ]
        V = Vs[g]
        O = p + 1
        R = O > 1 or g <= 2
        R = [0 if R else i % 2 + 1 for i in range(4)]
        self.value[V[0]], self.value[V[1]], self.value[V[2]], self.value[V[3]] = [
            [
                self.value[V[(i + O) % 4]][0],
                (self.value[V[(i + O) % 4]][1] + R[i]) % 3
            ]
            for i in range(4)
        ]
