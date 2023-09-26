class FileParse:
    def __init__(self, filename, context, execs={}):
        self.filename = filename
        self.execs = execs
        self.context = context
        self.parsed = []

    def parse(self):
        with open(self.filename, 'r') as f:
            self.parsed = [i.strip() for i in f.readlines()]

    def exec(self):
        for line in self.parsed:
            L = LineExec(self.context, self.execs)
            L.exec(line)

class LineExec:
    def __init__(self, context, execs={}):
        self.execs = execs
        self.context = context

    def exec(self, ln):
        line = ln.split(" ")
        print(self.context, line)
        if line[0] in self.execs:
            if len(line) == 1:
                self.execs[line[0]](self.context)
            else:
                self.execs[line[0]](self.context, *line[1:])
        else:
            self.execs["help"]()