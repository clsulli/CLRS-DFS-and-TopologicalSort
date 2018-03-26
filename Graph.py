class Graph:
    def __init__(self):
        self.G = {}
        self.color = {}
        self.pi = {}
        self.discovered = {}
        self.finished = {}
        self.acyilic = True


    def addVertice(self, vertList):
        self.G[vertList[0]] = [vertList[0],vertList[1],vertList[2]]

    def getVertice(self, Idx):
        return self.G[Idx]

    def getGraph(self):
        return self.G