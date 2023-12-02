from randomisedRounder import randomisedRounder
from Solver import maxWeight

#x is solution of relaxed matrix
def runMajorityAlgo(x,fileName,iterationCount,reductionFactor):

    currentSolution = maxWeight(randomisedRounder(x),fileName)
    n = len(x)
    m = len(x[0])
    for i in range(iterationCount):
        #print("current solution is "+str(currentSolution))
        tempMatrix = randomisedRounder(x)
        newSolution = maxWeight(tempMatrix,fileName)

        if newSolution>currentSolution:
            for row in range(n):
                rowSum = 0
                for col in range(m):
                    if tempMatrix[row][col]==1:
                        x[row][col] = (1-reductionFactor)*x[row][col]
                    rowSum+=x[row][col]
                for col in range(m):
                    x[row][col] = x[row][col]/rowSum
        else:
            currentSolution = newSolution
    #print("current solution is "+str(currentSolution))
    return currentSolution

def analyseMajoritySolver(x,fileName,reductionFactor,correctSolution,maxAllowedIterations):
    currentSolution = maxWeight(randomisedRounder(x),fileName)
    if currentSolution==correctSolution:
        return 1
    n = len(x)
    m = len(x[0])
    i=1
    while i<maxAllowedIterations:
        #print("current solution is "+str(currentSolution))
        i+=1
        tempMatrix = randomisedRounder(x)
        newSolution = maxWeight(tempMatrix,fileName)

        if newSolution>currentSolution:
            for row in range(n):
                rowSum = 0
                for col in range(m):
                    if tempMatrix[row][col]==1:
                        x[row][col] = (1-reductionFactor)*x[row][col]
                    rowSum+=x[row][col]
                for col in range(m):
                    x[row][col] = x[row][col]/rowSum
        else:
            currentSolution = newSolution
        if currentSolution==correctSolution:
            break
    #print("current solution is "+str(currentSolution))
    return i     