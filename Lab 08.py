G = {}
nodes = [0, 1, 2, 3, 4, 5]
directed = False
node = 3
Node1 = 1
Node2 = 2
def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G
G = addNodes(G, nodes)

edges = [(0, 1, 1), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 4, 1), (3, 4, 1), (3, 5, 1), (4, 5, 1)] 
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
G = addEdges(G, edges, directed)

def listOfNodes(G):
    l = []
    for i in G:
        l.append(i)
    return l
print(listOfNodes(G))

def listOfEdges(G, directed):
    l = []
    for i in G:
        u1 = i
        if len(G[i]) > 0:
            size = len(G[i])
            for j in range(size):
                v1 = G[i][j][0]
                w1 = G[i][j][1]
                t = (u1, v1, w1)
                if (v1, u1, w1) not in l:
                    l.append(t)
    return l
print(listOfEdges(G, directed))

def printIn_OutDegree(G):
    for k in G:
        In = 0
        for i in G:
            Out = len(G[k])
            for j in G[i]:
                if j[0] == k:
                    In += 1
        print (k, '=> In-Degree:', str(In) + ', Out-Degree:', Out)
printIn_OutDegree(G)

def printDegree(G):
    for i in G:
        print (i, '=>', len(G[i]))
printDegree(G)

def getNeighbors(G, node): 
  l = []
  for i in G[node]:
    l.append(i[0])
  return l
print(getNeighbors(G, node))

def getInNeighbors(G, node):
  l = []
  for i in G:
    for j in G[i]:
      if j [0]== node:
        l.append(i)
  return l
print(getInNeighbors(G, node))

def getOutNeighbors(G, node):
    l = []
    for i in G[node]:
        l.append(i[0])
    return l
print (getOutNeighbors(G, node))

def getNearestNeighbor(G, node):
    lw = G[node][0][1]
    n = G[node][0][0]
    for i in G[node]:
        if i[1] < lw:
            lw = i[1]
            n = i[0]
    return n
print(getNearestNeighbor(G, node))

def isNeighbor(G, Node1, Node2):
    for i in G[Node1]:
        if i[0] == Node2:
            return True
    return False
print(isNeighbor(G, Node1, Node2))

def removeNode(G, node):
    l = len(G)
    for i in range(l):
        if i in G:
            if i == node:
                del G[i]
            else:
                for j in G[i]:
                    if j[0] == node:
                        G[i].remove(j)
    return G
G = removeNode(G, node)

def removeNodes(G, nodes):
    for i in nodes:
        if i in G:
            removeNode(G, i)
    return G
        
G = removeNodes(G, nodes)

def displayGraph(G):
  print (G)
displayGraph(G)

def display_adj_matrix(G):
  l = []
  for i in G:
    l2 = []
    for j in G:
        x = False
        for k in G[i]:
            if k[0] == j:
                x = True
                l2.append(k[1])
        if x == False:
            l2.append(0)
    l.append(l2)
  print (l)
display_adj_matrix(G)
