import random

def randomisedRounder(x):
    """
    Rounds the fractional assignment of variables using the randomised scheme described in the paper
 
    Args:
        x (2D array): Fractional optimum solution to the LP
 
    Returns:
        xRounded (2D array): Integral solution obtained by rounding x
    """
    
    numberOfNets = len(x)
    treesPerNet = len(x[0])
    #Initialise xRounded to all 0s:
    xRounded = []
    for i in range(numberOfNets):
        xRounded.append([0]*treesPerNet)
    for i in range(numberOfNets):
        #Array to keep track of the variables that have been rounded to 1
        roundedUpPosns = []
        positivePosns = []
        for j in range(treesPerNet):
            if x[i][j] > 0:
                #Round to 1 with probability x[i][j] 
                positivePosns.append(j)
                randVal = random.random()
                if randVal <= x[i][j]:
                    roundedUpPosns.append(j)
        #Choose one of the rounded up variables u.a.r and set only it to 1 to keep the rounding exclusive
        if len(roundedUpPosns) > 1:
            chosenPosn = random.choice(roundedUpPosns)
            xRounded[i][chosenPosn] = 1
        else:
            chosenPosn = random.choice(positivePosns)
            xRounded[i][chosenPosn] = 1

    return xRounded

'''
def getInput():
    numberOfNets = int(input())
    treesPerNet = int(input())
    inputMatrix = []
    for i in range(numberOfNets):
        treeProbabilities = []
        for j in range(treesPerNet):
            treeProbabilities.append(int(input()))
        numberOfNets.append(treeProbabilities)
    return inputMatrix

def solve():
    return randomisedRounder(getInput())

solve()

'''
