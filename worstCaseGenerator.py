import sys

stdout_fileno = sys.stdout

def writer(x):
    sys.stdout.write(str(x) + '\n')

def generateWorstCaseInput(fileName, n):
    sys.stdout = open(fileName, 'w')
    writer(n)
    writer(n-1)
    writer(n)
    for i in range(0,n-1):
        for j in range(0,n):
            edges = []
            currPos = [0, i]
            while currPos[1] != j:
                if j < currPos[1]:
                    edges.append([currPos[0], currPos[1], 0, currPos[1]-1])
                    currPos[1] -= 1
                else:
                    edges.append([currPos[0], currPos[1], 0, currPos[1]+1])
                    currPos[1] += 1
            while currPos[0] != n-1:
                edges.append([currPos[0], currPos[1], currPos[0]+1, currPos[1]])
                currPos[0] += 1
            while currPos[1] != i:
                if i > currPos[1]:
                    edges.append([currPos[0], currPos[1], currPos[0], currPos[1]+1])
                    currPos[1] += 1
                else:
                    edges.append([currPos[0], currPos[1], currPos[0], currPos[1]-1])
                    currPos[1] -= 1
            writer(len(edges))
            for edge in edges:
                writer(" ".join([str(el) for el in edge]))
    sys.stdout.close()
    sys.stdout = stdout_fileno
