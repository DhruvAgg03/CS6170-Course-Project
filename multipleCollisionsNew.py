import random
import sys
import Input_generator

def writer(x):
    sys.stdout.write(x)

def inputWithCollidingEdgeSet(fileName,N,netCount,treesPerNet,edgeSetSize):
    stdout_fileno = sys.stdout
    sys.stdout = open(fileName, 'w')
    random.seed()
    writer(str(N)+"\n")
    writer(str(netCount)+"\n")
    writer(str(treesPerNet)+"\n")
    treesPerNet -= 1
    edgeSet = []
    extraEdge = []
    
    edgeSetSize = treesPerNet + 1
    extra = netCount // edgeSetSize + 1
    for i in range(edgeSetSize + extra):
        randX1 = random.randint(1,N-2)
        randY1 = random.randint(1,N-2)
        d = random.randint(1,4) #direction
        if d==1:
            randX2 = randX1 + 1
            randY2 = randY1
        elif d==2:
            randX2 = randX1 - 1 
            randY2 = randY1
        elif d==3:
            randX2 = randX1
            randY2 = randY1 + 1
        else:
            randX2 = randX1
            randY2 = randY1 - 1
        
        if i >= edgeSetSize:
            extraEdge.append(Input_generator.Edge(Input_generator.Coordinate(randX1,randY1),Input_generator.Coordinate(randX2,randY2)))
        else:
            edgeSet.append(Input_generator.Edge(Input_generator.Coordinate(randX1,randY1),Input_generator.Coordinate(randX2,randY2)))
    
    for i in range(netCount):
        for j in range(treesPerNet):
            tree = [edgeSet[(i*treesPerNet + j)%edgeSetSize]]
            Input_generator.PrintTree(tree)
        cnt = i//edgeSetSize
        tree = [extraEdge[cnt]]
        Input_generator.PrintTree(tree)
    
    sys.stdout.close()
    sys.stdout = stdout_fileno
    return 0

def printTreesToFile(fileName,N,netCount,treesPerNet,edgeSetSize):
    inputWithCollidingEdgeSet(fileName,N,netCount,treesPerNet,edgeSetSize)