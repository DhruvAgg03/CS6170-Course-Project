from Input_generator import printTreesToFile as randomTrees
from Solver import solver
from Solver import maxWeight
from randomisedRounder import randomisedRounder 
from multipleCollisionsNew import printTreesToFile as collidingTrees
from worstCaseGenerator import generateWorstCaseInput as worstCaseTrees
from majority_algorithm import runMajorityAlgo as majorityAlgorithm
from majority_algorithm import analyseMajoritySolver
import time
from math import log2
from math import ceil

N = 30
netCount = 50
treesPerNet = 4
inputFileName = 'output.txt'
collisionEdgeSetSize = 3
majorityAlgorithmIterations = 10
majorityReductionFactor = 0.3

#inputType
#0 - random
#1 - colliding
#2 - worst case

def GenerateInput(inputType):
    global N, netCount,treesPerNet
    if inputType==0:
        randomTrees(inputFileName,N,netCount,treesPerNet)
    elif inputType==1:
        collidingTrees(inputFileName,N,netCount,treesPerNet,collisionEdgeSetSize)
    elif inputType==2:
        worstCaseTrees(inputFileName,N)
    else:
        print("INVALID input type")
        exit(1)


#solver type
#0 - ILP
#1 - relaxed
#2 - randomised rounder
#3 - majority
def Solve(solverType): #returns optimal value from solver
    if solverType==0:
        optimalIntegerSolution,integerMatrix = solver(inputFileName,0)
        return optimalIntegerSolution
    elif solverType==1:
        optimalRelaxedSolution,relaxedMatrix = solver(inputFileName,1)
        return optimalRelaxedSolution
    elif solverType==2:
        optimalRelaxedSolution,relaxedMatrix = solver(inputFileName,1)
        return maxWeight(randomisedRounder(relaxedMatrix),inputFileName)
    elif solverType==3:
        optimalRelaxedSolution,relaxedMatrix = solver(inputFileName,1)
        return majorityAlgorithm(relaxedMatrix,fileName,majorityAlgorithmIterations,majorityReductionFactor)


def matchingProbability(optimal, randomisedOutputs):
    total = len(randomisedOutputs)
    count = 0
    for output in randomisedOutputs:
        if output==optimal:
            count+=1
    return count/total

def listAverage(lst):
    sum = 0
    for i in range(len(lst)):
        sum+=lst[i]
    return sum/len(lst)

#Find num of iterations it takes for rounder to get correct solution
maxAllowedIterations = 65 #for one round
totalIterationsProbability = 10
#inputType
#0 - random
#1 - colliding
#2 - worst case

#solve type
#0 - randomised rounder
#1 - majority
def solveForInputType(inputType,solveType):
    #On randomised inputs
    '''
    if inputType==0:
        print("Testing on random input")
    elif inputType==1:
        print("Testing on colliding input")
    elif inputType==2:
        print("Testing on worst case input")
    else:
        print("Invalid input")
    '''
    probabilityList = []
    
    if solveType==0: #randomised rounder
        for i in range(totalIterationsProbability):
            GenerateInput(inputType)
            #print("input gen done")
            optimalIntegerSolution = Solve(0)
            #print("Optimal integer Solution is "+str(optimalIntegerSolution))
            optimalRelaxedSolution,relaxedMatrix = solver(inputFileName,1)
            #print(relaxedMatrix)
            iterationsTillMatching = 0
            j=0
            while j<maxAllowedIterations:
                iterationsTillMatching+=1
                roundedSolution = maxWeight(randomisedRounder(relaxedMatrix),inputFileName)
                if roundedSolution==optimalIntegerSolution:
                    break
                #print("solution reached is "+str(roundedSolution))
                j+=1
            probabilityList.append(iterationsTillMatching)
            '''
            if j<maxAllowedIterations:
                print("Solved iteration "+str(i)+" with "+str(iterationsTillMatching))
            else:
                print("Did not reach solution")
            '''
    elif solveType==1: #majority solver
        for i in range(totalIterationsProbability):
            GenerateInput(inputType)
            optimalIntegerSolution = Solve(0)
            #print("Optimal integer Solution is "+str(optimalIntegerSolution))
            optimalRelaxedSolution,relaxedMatrix = solver(inputFileName,1)
            iterationsRequired = analyseMajoritySolver(relaxedMatrix,inputFileName,0.3,optimalIntegerSolution,maxAllowedIterations)
            probabilityList.append(iterationsRequired)
            '''
            if iterationsRequired<maxAllowedIterations:
                print("Solved iteration "+str(i)+" with "+str(iterationsRequired))
            else:
                print("Did not reach solution")
    
            '''
    avg = listAverage(probabilityList)
    #print(avg)
    return avg



#inputType
#0 - random
#1 - colliding
#2 - worst case

#solve type
#0 - randomised rounder
#1 - majority

#for varying netCount, fixed trees Per net
def varyNetCount(inputType,solveType):
    global treesPerNet,netCount
    treesPerNet = 6
    for i in range (10,25):
        startTime = time.time()
        netCount = i
        print(str(i)+","+str(solveForInputType(inputType,solveType)))
        endTime = time.time()
        runningTime = endTime - startTime
        print(runningTime)

def varyTreesPerNet(inputType,solveType):
    global treesPerNet,netCount
    netCount = 10
    for i in range(5,15):
        treesPerNet = i
        print(str(i)+","+str(solveForInputType(inputType,solveType)))

#varyNetCount(0,1)

#generate 1 input
#find integer optimal
#get relaxed solution
#run MWU on it multiple times with varying eta
def checkingEta(inputType):
    GenerateInput(inputType)
    optimalIntegerSolution = Solve(0)
    optimalRelaxedSolution,relaxedMatrix = solver(inputFileName,1)
    sol1 = analyseMajoritySolver(relaxedMatrix,inputFileName,0.2,optimalIntegerSolution,maxAllowedIterations)
    sol11 = analyseMajoritySolver(relaxedMatrix,inputFileName,0.3,optimalIntegerSolution,maxAllowedIterations)
    sol2 = analyseMajoritySolver(relaxedMatrix,inputFileName,0.4,optimalIntegerSolution,maxAllowedIterations)
    sol3 = analyseMajoritySolver(relaxedMatrix,inputFileName,0.6,optimalIntegerSolution,maxAllowedIterations)
    sol4 = analyseMajoritySolver(relaxedMatrix,inputFileName,0.9,optimalIntegerSolution,maxAllowedIterations)
    print(str(sol1)+","+str(sol11)+","+str(sol2)+","+str(sol3)+","+str(sol4))

def multipleEtaCheck(iterations,inputType):
    for i in range(iterations):
        checkingEta(inputType)

#dense trees: NxN, N trees per net, N nets
# N varies from 5 to 30
#allowing 5 iterations in 5 MWU
def denseGridAnalysisForEta(eta,relaxedMatrix):
    return majorityAlgorithm(relaxedMatrix,inputFileName,5,eta)

def denseAnalysisEta(nValue):
    global N,treesPerNet,  netCount
    N = nValue
    treesPerNet = ceil(log2(N))
    netCount = ceil(log2(N))
    GenerateInput(2)
    optimalIntegerSolution = Solve(0)
    optimalRelaxedSolution, relaxedMatrix = solver(inputFileName,1)
    #print("For eta = 0.2")
    print(str(nValue)+","+str(denseGridAnalysisForEta(0.2,relaxedMatrix)/optimalIntegerSolution)+",0.2")
    print(str(nValue)+","+str(denseGridAnalysisForEta(0.3,relaxedMatrix)/optimalIntegerSolution)+",0.3")
    print(str(nValue)+","+str(denseGridAnalysisForEta(0.6,relaxedMatrix)/optimalIntegerSolution)+",0.6")
    print(str(nValue)+","+str(denseGridAnalysisForEta(0.8,relaxedMatrix)/optimalIntegerSolution)+",0.8")

for i in range(5,31):
    denseAnalysisEta(i)