from Board import *
from AStar import *
from FileParse import *

def getDefContext(): 
    return {
        "puzzle": Board(),
        "node_limit": 1000000000
    }

def solve(context, type, arg):
    if type == "A-star":
        F = AStar.Heuristics.h0 if arg == "h0" else AStar.Heuristics.h1 if arg == "h1" else AStar.Heuristics.h2
        B = AStar(F, context["puzzle"], Board(), nodeLimit=context["node_limit"])
    elif type == "beam":
        B = AStar(AStar.Heuristics.h2, context["puzzle"], Board(), beamLimit=int(arg), nodeLimit=context["node_limit"])
    
    B.solve()
    print(B.getSolution())

def maxNodes(context, n):
    context["node_limit"] = n

def readFile(_, f):
    F = FileParse(f, getDefContext(), execs=FUNCTIONS)
    F.parse()
    print(F.parsed)
    F.exec()

def help(_=None):
    print("Available functions:")
    for f in FUNCTIONS:
        print(f)
    print("quit")

FUNCTIONS = {
    "setState": lambda context, state: context["puzzle"].setState(state),
    "printState": lambda context: context["puzzle"].printState(),
    "move": lambda context, move: context["puzzle"].move(move),
    "randomizeState": lambda context, n: context["puzzle"].randomizeState(int(n)),
    "solve": solve,
    "maxNodes": maxNodes,
    "readFile": readFile,
    "help": help
}

c = getDefContext()

while True:
    i = input("> ")
    if ("quit" in i):
        break
    line = LineExec(c, FUNCTIONS)
    line.exec(i)
