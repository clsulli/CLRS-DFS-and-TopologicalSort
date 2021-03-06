import time
from Graph import Graph
from LinkedList import LinkedList

def fileSelection():
    print("Specify input file or use Sample file?")
    print("     (a) Specify input file")
    print("     (b) Sample file")

    dataIn = raw_input(">> ")

    if dataIn == "a" or dataIn == "A":
        print("Enter filename (Include the .txt):")
        filename = raw_input(">> ")
        filename = "InputFiles/" + filename
        return filename
    elif dataIn == "b" or dataIn == "B":
        filename = "InputFiles/graphin.txt"
        return filename
    else:
        print("Incorrect Input.  Please try again.\n")
        fileSelection()

def createGraph(file):
    G = Graph()

    fileO = open(file, "r")
    for line in fileO:
        currLine = line.strip("\n")
        currLine = currLine.strip(":")
        currLine = currLine.split(" ")
        vertice = int(currLine[0][0])
        edgeList = []
        ##first item in edgeList is root Vertex
        for item in range(1, len(currLine)):
            edgeV = int(currLine[item])
            edgeList.append(edgeV)

        G.addVE(vertice, edgeList)

    return G

def dfsVisit(G, u):
    global cTime
    cTime = cTime + 1
    g = G.getGraph()
    G.discovered[u] = cTime
    G.color[u] = "gray"

    for v in g[u]:
        if G.color[v] == "white":
            G.pi[v] = u
            dfsVisit(G, v)

        elif G.color[v] == "gray":
            G.acyilic=False

    G.color[u] = "black"
    cTime = cTime + 1
    G.finished[u] = cTime

def dfsVisitT(G, u):
    global cTime
    global topoList
    cTime = cTime + 1
    g = G.getGraph()
    G.discovered[u] = cTime
    G.color[u] = "gray"

    for v in g[u]:
        if G.color[v] == "white":
            G.pi[v] = u
            dfsVisitT(G, v)

        elif G.color[v] == "gray":
            G.acyilic=False

    topoList.add(u)
    G.color[u] = "black"
    cTime = cTime + 1
    G.finished[u] = cTime

def dfs(G):
    global cTime
    g = G.getGraph()
    for u in g:
        G.color[u] = "white"
        G.pi[u] = "nil"
    cTime = 0
    for u in g:
        if G.color[u] == "white":
            dfsVisit(G, u)

def dfsT(G):
    global cTime
    global topoList
    g = G.getGraph()
    for u in g:
        G.color[u] = "white"
        G.pi[u] = "nil"
    cTime = 0
    for u in g:
        if G.color[u] == "white":
            dfsVisitT(G, u)

def topoSort(G):
    global topoList
    dfsT(G)
    topoList.printList()

def genEdges(G):
    g = G.getGraph()
    allEdges = []
    backEdges = []

    for u in g:
        for v in g[u]:
            edges = {u:v}
            allEdges.append(edges)

    for edge in allEdges:
        u = list(edge.keys())[0]
        v = list(edge.values())[0]

        if G.discovered[v] < G.discovered[u] and G.discovered[u] < G.finished[v] and G.finished[u] < G.finished[v]:
            backEdges.append(edge)

    print("     Back Edges:")
    for edge in backEdges:
        bu = list(edge.keys())[0]
        bv = list(edge.values())[0]

        print("     (" + str(bu) + "," + str(bv) + ")")

cTime = 0
topoList = LinkedList()

currFile = fileSelection()
G = createGraph(currFile)

print("     Running DFS...")
dfs(G)
print("     DFS Completed.")

if G.acyilic == True:
    print("Graph is Acylic, running Topological Sort")
    print("     Graph in Topological Order: (0 = Start)")
    topoSort(G)
elif G.acyilic == False:
    print("Graph is not Acylic")
    genEdges(G)












