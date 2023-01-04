
def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G
def addEdges(G, edges, directed):
    for i in edges:
        u1 = i[0]
        if len(i) < 3:
          t = (i[1], 1)
        else:
          t = (i[1], i[2])
        G[u1].append(t)
        if directed == False:
            v1 = i[1]
            if len(i) < 3:
              t = (i[0], 1)
            else:
              t = (i[0], i[2])
            G[v1].append(t)
    return G

def listOfNodes(G):
    l = []
    for i in G:
        l.append(i)
    return l


graph = {}
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
addNodes(graph, nodes)

edges = [('A', 'B', 5), ('A', 'E', 6), ('A', 'D', 3), ('B', 'C', 6), ('C', 'D', 10), ('C', 'G', 2), ('D', 'F', 8), ('E', 'F', 9), ('F', 'G', 10)]
addEdges(graph, edges, directed = False)

source = 'A'
destination = 'G'

def getShortestPath(G, source, destination):
    ListOfNodes = list(G.keys())
    infinity = 9999
    ShortestDistance = []
    #queue = []
    for i in ListOfNodes:
        if i == source:
            ShortestDistance.append([source, source, 0]) 
        else:
            ShortestDistance.append(["", i, infinity])
    UNVISITED = ListOfNodes.copy()
    VISITED = []
    #push(queue, (source, 0))
    while UNVISITED:
        lowest_distance = infinity
        Current_Vertex = ""
        for j in range(len(ShortestDistance)):
            print (j)
            if ShortestDistance[j][2] <= lowest_distance and ShortestDistance[j][1] not in VISITED:
                lowest_distance = ShortestDistance[j][2] 
                Current_Vertex = ShortestDistance[j][1]
        for k in G[Current_Vertex]:
          print (k, ShortestDistance)
          if k[0] not in VISITED:
            if ShortestDistance[k][2] > (ShortestDistance[Current_Vertex][2] + k[1]):
              ShortestDistance[k][2] = (ShortestDistance[Current_Vertex][2] + k[1])
              ShortestDistance[k][0] = Current_Vertex
        pop(UNVISITED)
        push(VISITED, Current_Vertex)
    return VISITED
print(getShortestPath(graph, source, destination))