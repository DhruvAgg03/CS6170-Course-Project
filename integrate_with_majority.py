from Input_generator import printTreesToFile
from Solver import solver
from majority_algorithm import runMajorityAlgo

N = 30
netCount = 2
treesPerNet = 3

def matchingProbability(optimal, randomisedOutputs):
    total = len(randomisedOutputs)
    count = 0
    for output in randomisedOutputs:
        if output==optimal:
            count+=1
    return count/total

def main():
    fileName = "output.txt"
    printTreesToFile(fileName,N,netCount,treesPerNet)
    optimalIntegerSolution,integerMatrix = solver(fileName,0)
    optimalRelaxedSolution,relaxedMatrix = solver(fileName,1)
    iterationCount = 100

    randomisedSolutions = []
    for i in range(iterationCount):
        randomisedOptimalSolution = runMajorityAlgo(relaxedMatrix,fileName)
        randomisedSolutions.append(randomisedOptimalSolution)
        print("Optimal Integer Solution: "+str(optimalIntegerSolution)+"\nRandomised Integer Solution: "+str(randomisedOptimalSolution))
    print("Accuracy: "+str(matchingProbability(optimalIntegerSolution,randomisedSolutions)))


if __name__=="__main__": 
    main() 