from typing import NamedTuple
import sys
import random
from queue import Queue  

stdout_fileno = sys.stdout

chooseParameter = 0.8
N=0
def writer(x):
    sys.stdout.write(x)

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def getMinCoord(coord1,coord2):
    if coord1.x<coord2.x or (coord1.x==coord2.x and coord1.y<coord2.y):
        return coord1
    else:
        return coord2

def getMaxCoord(coord1,coord2):
    if coord1.x>coord2.x or (coord1.x==coord2.x and coord1.y>coord2.y):
        return coord1
    else:
        return coord2
    
class Edge:
    def __init__(self,coord1,coord2):
        self.coord1 = getMinCoord(coord1,coord2)
        self.coord2 = getMaxCoord(coord1,coord2)

def IsValidCoordinate(coord,N):
    return coord.x>=0 and coord.x<N and coord.y>=0 and coord.y<N

def PrintTree(tree):
    writer(str(len(tree))+"\n")
    for edge in tree:
        writer(str(edge.coord1.x) +" "+str(edge.coord1.y)+" "+str(edge.coord2.x)+" "+str(edge.coord2.y)+"\n")

def GenerateRandomTree(N,chooseParameter):
    tree=[]
    randX = random.randint(0,N-1)
    randY = random.randint(0,N-1)
    treeDepth = random.randint(0,int(N/2)-1)+int(N/4)
    marked = []
    inBFS=[]
    for i in range(N):
        initers = []
        for j in range(N):
            initers.append(False)
        marked.append(initers)
        inBFS.append(initers)
    bfs = Queue()
    currentDepth = 0
    bfs.put(Coordinate(randX,randY))
    inBFS[randX][randY] = True
    while (not bfs.empty()) and currentDepth<treeDepth:
        size = bfs.qsize()
        for i in range(size):
            current = bfs.get()
            inBFS[current.x][current.y] = False
            if(currentDepth>treeDepth/2) and (random.randint(0,100)>chooseParameter*100):
                continue
            if marked[current.x][current.y]:
                writer("ERROR: Already Marked" + str(current.x)+" "+str(current.y)+"\n")
                continue
            marked[current.x][current.y] = True
            if IsValidCoordinate(Coordinate(current.x+1,current.y),N) and (not marked[current.x+1][current.y]):
                bfs.put(Coordinate(current.x+1,current.y))
                inBFS[current.x+1][current.y] = True
                tree.append(Edge(current,Coordinate(current.x+1,current.y)))
            if IsValidCoordinate(Coordinate(current.x-1,current.y),N) and (not marked[current.x-1][current.y]):
                bfs.put(Coordinate(current.x-1,current.y))
                inBFS[current.x-1][current.y] = True
                tree.append(Edge(current,Coordinate(current.x-1,current.y)))
            if IsValidCoordinate(Coordinate(current.x,current.y+1),N) and (not marked[current.x][current.y+1]):
                bfs.put(Coordinate(current.x,current.y+1))
                inBFS[current.x][current.y+1] = True
                tree.append(Edge(current,Coordinate(current.x,current.y+1)))
            if IsValidCoordinate(Coordinate(current.x,current.y-1),N) and (not marked[current.x][current.y-1]):
                bfs.put(Coordinate(current.x,current.y-1))
                inBFS[current.x][current.y-1] = True
                tree.append(Edge(current,Coordinate(current.x,current.y-1)))
        currentDepth+=1
    return tree


def GenerateRandomTree2(N,chooseParameter):
    #choose parameter not needed. only added because it was used everywhere
    tree = []
    randX = random.randint(0,N-1)
    randY = random.randint(0,N-1)
    treeSize = random.randint(N,N^2)
    marked = []
    neighbours=[]
    for i in range(N):
        initers = []
        for j in range(N):
            initers.append(False)
        marked.append(initers)
        inBFS.append(initers)

    nodesAdded = 0
    neighbours.append(Coordinate(randX,randY))
    while nodesAdded<treeSize:
        currentNode = neighbours[0]
        neighbours.pop(0)
        if marked[currentNode.x][currentNode.y]:
            continue
        nodesAdded+=1
        marked[currentNode.x][currentNode.y] = True
        if IsValidCoordinate(Coordinate(currentNode.x+1,currentNode.y)) and (not marked[currentNode.x+1][currentNode.y]):
            newNode = Coordinate(currentNode.x+1,currentNode.y)
            tree.append(Edge(currentNode,newNode))
        if IsValidCoordinate(Coordinate(currentNode.x-1,currentNode.y)) and (not marked[currentNode.x-1][currentNode.y]):
            newNode = Coordinate(currentNode.x-1,currentNode.y)
        if IsValidCoordinate(Coordinate(currentNode.x,currentNode.y+1)) and (not marked[currentNode.x][currentNode.y+1]):
            newNode = Coordinate(currentNode.x,currentNode.y+1)
        if IsValidCoordinate(Coordinate(currentNode.x,currentNode.y-1)) and (not marked[currentNode.x][currentNode.y-1]):
            newNode = Coordinate(currentNode.x,currentNode.y-1)

def printTreesToFile(fileName,M,netCount,treesPerNet):
    global N
    N=M
    sys.stdout = open(fileName, 'w')
    random.seed()
    writer(str(N)+"\n")
    writer(str(netCount)+"\n")
    writer(str(treesPerNet)+"\n")
    for i in range(netCount):
        for j in range(treesPerNet):
            PrintTree(GenerateRandomTree(N,chooseParameter))
    sys.stdout.close()
    sys.stdout = stdout_fileno
    return 0

