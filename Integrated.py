from Input_generator import printTreesToFile
from Solver import solver
from Solver import maxWeight
from randomisedRounder import randomisedRounder
from multipleCollisions import printTreesToFile

N = 5
netCount = 30
treesPerNet = 5

def matchingProbability(optimal, randomisedOutputs):
    total = len(randomisedOutputs)
    count = 0
    for output in randomisedOutputs:
        if output==optimal:
            count+=1
    return count/total



def main():
    fileName = "output.txt"
    #printTreesToFile(fileName,N,netCount,treesPerNet)
    printTreesToFile(fileName,N,netCount,treesPerNet,2)
    optimalIntegerSolution,integerMatrix = solver(fileName,0)
    optimalRelaxedSolution,relaxedMatrix = solver(fileName,1)
    
    '''
    iterationCount = 1000
    count=0
    for i in range(iterationCount):
        opt,tempMatrix =solver(fileName,1)
        if tempMatrix==relaxedMatrix:
            count+=1
    print(count)
    '''
    iterationCount=1000
    randomisedSolutions = []
    for i in range(iterationCount):
        randomisedIntegerMatrix = randomisedRounder(relaxedMatrix)
        randomisedOptimalSolution = maxWeight(randomisedIntegerMatrix,fileName)
        randomisedSolutions.append(randomisedOptimalSolution)
        print("Optimal Integer Solution: "+str(optimalIntegerSolution)+"\nRandomised Integer Solution: "+str(randomisedOptimalSolution)+"\nRational solution:"+str(optimalRelaxedSolution))
    print("Accuracy: "+str(matchingProbability(optimalIntegerSolution,randomisedSolutions)))

if __name__=="__main__": 
    main() 