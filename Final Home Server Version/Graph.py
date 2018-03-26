class Graph:
    def __init__(self):
        self.G = {}
        self.color = {}
        self.pi = {}
        self.discovered = {}
        self.finished = {}
        self.acyilic = True

    def addVE(self, V, E):
        self.G[V] = E

    def getGraph(self):
        return self.G