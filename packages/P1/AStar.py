import heapq
from Board import *

class AStar:
    class AStarNode:
        def __init__(self, state, parent=None, cost=0, action=""):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost

        def __lt__(self, other):
            return self.cost < other.cost

        def __str__(self):
            return str(self.action) + " " + str(self.cost) + "\n" + str(self.state)

        def __repl__(self):
            return str(self)

        def getNeighbors(self):
            def makeNeighbor(val, i):
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
        @staticmethod
        def h0(a: Board, goal: Board):
            return a.value != goal.value

        @staticmethod
        def h1(a: Board, goal: Board):
            return sum([sum([a.value[i][j] != goal.value[i][j] and a.value[i][j] != 0 for j in range(len(a.value[i]))]) for i in range(len(a.value))])

        @staticmethod
        def h2(a: Board, goal: Board):
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
        if (self.solution is not None):
            o = []
            node = self.solution

            while node is not None:
                o.append(node.action)
                node = node.parent

            return str(len(o))+":"+" ".join(reversed(o))

    def iterate(self):
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
        limit = limit if limit is not None else self.nodeLimit
        for _ in range(limit):
            a = self.iterate()
            if a:
                return True

        return False
