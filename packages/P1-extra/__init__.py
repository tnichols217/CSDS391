from Board import *
from Rubiks import *
from AStar import *
from FileParse import *
import sys

# def getDefContext():
#     """Create Default Context for Command Line Interface"""
#     return {
#         "puzzle": Board(),
#         "node_limit": 1000000000,
#         "seed": 12497989,
#         "show_time": False
#     }

# def setState(context, *state):
#     """(state): Set State Wrapper for merging multiple args into a single string"""
#     context["puzzle"].setState("".join(state))

# def solve(context, type, arg):
#     """(algorithm, arg): Solver Wrapper and heuristic picker for A-star and Beam Search"""
#     if type == "A-star":
#         F = AStar.Heuristics.h0 if arg == "h0" else AStar.Heuristics.h1 if arg == "h1" else AStar.Heuristics.h2
#         B = AStar(F, context["puzzle"], Board(), nodeLimit=context["node_limit"])
#     elif type == "beam":
#         B = AStar(AStar.Heuristics.h2, context["puzzle"], Board(), beamLimit=int(arg), nodeLimit=context["node_limit"])
    
#     B.solve()
#     print(B.getSolution())

# def maxNodes(context, n):
#     """(n): Set Node Limit for current Context to be used for the solver"""
#     context["node_limit"] = int(n)

# def setSeed(context, n):
#     """(n): Set the seed for the random number generator"""
#     context["seed"] = int(n)

# def showTime(context, n):
#     """(n): Choose whether to display the timer or not"""
#     context["show_time"] = (n == "True" or n == "true" or n == "t" or n == "T")

# def readFile(_, f):
#     """(file): Reads a file and immediately executes the specified functions"""
#     F = FileParse(f, getDefContext(), execs=FUNCTIONS)
#     F.parse()
#     print(F.parsed)
#     F.exec()

# def printState(context):
#     """(): Prints the current state of the puzzle"""
#     context["puzzle"].printState()

# def move(context, move):
#     """(move): Moves the current puzzle in one of the four cardinal directions"""
#     context["puzzle"].move(move)

# def randomizeState(context, n):
#     """(n): Generates a randomized state of the puzzle and sets it to the current puzzle"""
#     context["puzzle"].randomizeState(int(n), context["seed"])

# def help(_=None):
#     """(): Prints a list of available functions"""
#     print("Call each function with spaces between the function name and arguments")
#     print("Available functions:")
#     for f in FUNCTIONS:
#         print(f + FUNCTIONS[f].__doc__)
#     print("quit(): Quits the interactive shell")

# # Dictionary of available functions for the LineExec to run from
# FUNCTIONS = {
#     "setState": setState,
#     "printState": printState,
#     "move": move,
#     "randomizeState": randomizeState,
#     "solve": solve,
#     "maxNodes": maxNodes,
#     "setSeed": setSeed,
#     "showTime": showTime,
#     "readFile": readFile,
#     "help": help
# }

# # Get file passed in from command line
# if (len(sys.argv) > 1):
#     readFile(None, sys.argv[1])

# # Begin interactive shell
# c = getDefContext()
# line = LineExec(c, FUNCTIONS)

# while True:
#     i = input("> ")
#     if ("quit" in i):
#         break
#     try:
#         line.exec(i)
#     except Exception as e:
#         print(e)

a = Rubiks()
print(a.value)
a.move("F")
print(str(a))