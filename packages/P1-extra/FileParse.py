import time

class FileParse:
    """Reads a file and parses it for execution"""
    def __init__(self, filename, context, execs={}):
        self.filename = filename
        self.execs = execs
        self.context = context
        self.parsed = []

    def parse(self):
        """Parses the given file"""
        with open(self.filename, 'r') as f:
            self.parsed = [i.strip() for i in f.readlines()]

    def exec(self):
        """Executes all commands in the parsed file"""
        for line in self.parsed:
            L = LineExec(self.context, self.execs)
            L.exec(line)

class LineExec:
    """Executes a single line of code at a time on a given context"""
    def __init__(self, context, execs={}):
        self.execs = execs
        self.context = context

    def exec(self, ln):
        """Executes a single line of code"""
        line = ln.split(" ")
        print(self.context, line)
        a = time.time()
        if line[0] in self.execs:
            if len(line) == 1:
                self.execs[line[0]](self.context)
            else:
                self.execs[line[0]](self.context, *line[1:])
        else:
            self.execs["help"]()
        if self.context["show_time"]:
            print(str(int((time.time() - a)*1000)/1000) + "s ", end="")