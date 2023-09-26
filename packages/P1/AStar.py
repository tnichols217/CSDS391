import heapq
from Board import *

class AStar:
    """A-Star algorithm implementation for the 8-puzzle game"""
    class AStarNode:
        """A node in the A-Star search tree"""
        def __init__(self, state, parent=None, cost=0, action=""):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost

        def __lt__(self, other):
            """Backup for the priority queue sorting"""
            return self.cost < other.cost

        def __str__(self):
            return str(self.action) + " " + str(self.cost) + "\n" + str(self.state)

        def __repl__(self):
            return str(self)

        def getNeighbors(self):
            """Return all possible neighbors of this node"""
            def makeNeighbor(val, i):
                """Helper function to make a neighbor"""
                a = Board(val)
                a.move(i)
                return a

            return [
                AStar.AStarNode(
                    makeNeighbor(self.state.value, i),
                    self,
                    self.cost + 1,
                    i
                )
                for i
                in Board.directions
            ]

    class Heuristics:
        """Heuristics for the A-Star search tree"""
        @staticmethod
        def h0(a: Board, goal: Board):
            """Boolean heuristic for the A-Star search tree, zero if equal, one otherwise"""
            return a.value != goal.value

        @staticmethod
        def h1(a: Board, goal: Board):
            """Linear heuristic for the A-Star search tree, returns number of displaced tiles"""
            return sum([sum([a.value[i][j] != goal.value[i][j] and a.value[i][j] != 0 for j in range(len(a.value[i]))]) for i in range(len(a.value))])

        @staticmethod
        def h2(a: Board, goal: Board):
            """More accurate heuristic for the A-Star search tree, returns sum of distance to goal of each tile"""
            def coordDistance(a: tuple[int, int], goal: tuple[int, int]):
                return abs(a[0] - goal[0]) + abs(a[1] - goal[1])
            return sum([coordDistance(a.findValue(i), goal.findValue(i)) for i in range(9)])

    def __init__(self, heuristic=Heuristics.h1, state:Board=Board(), goalState:Board=Board(), beamLimit:int=0, nodeLimit:int=1000000):
        self.heuristic = heuristic
        self.initState = state.__copy__()
        self.queue:list[AStar.AStarNode] = []
        self.visited = []
        self.visited.append(self.initState.value)
        heapq.heappush(self.queue, (0, AStar.AStarNode(self.initState)))
        self.goalState = goalState
        self.solution: AStar.AStarNode = None
        self.beamLimit = beamLimit
        self.nodeLimit = nodeLimit

    def getSolution(self):
        """Parse the stored solution node and return it as a string"""
        if (self.solution is not None):
            o = []
            node = self.solution

            while node is not None:
                o.append(node.action)
                node = node.parent

            # Minus one as the root node has no action, and reverse as be begin at the solved state
            return str(len(o) - 1)+":"+" ".join(reversed(o))

    def iterate(self):
        """Discover one tile according to the A-Star heuristics, and add it to the queue"""
        _, node = heapq.heappop(self.queue)
        if node.state.value == self.goalState.value:
            self.solution = node
            return True

        for neighbor in node.getNeighbors():
            if neighbor.state.value in self.visited:
                continue

            self.visited.append(neighbor.state.value)

            heapq.heappush(self.queue, (neighbor.cost + self.heuristic(neighbor.state, self.goalState), neighbor))
        
        if self.beamLimit > 0:
            self.queue = self.queue[:self.beamLimit]

    def solve(self, limit:int=None):
        """Iterates through nodes until a solution is found or the limit is reached"""
        limit = limit if limit is not None else self.nodeLimit
        for _ in range(limit):
            a = self.iterate()
            if a:
                return True

        return False
