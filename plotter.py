import matplotlib.pyplot as plt

fileName = "etaCheckWorstInputVaryNSparse"
outName = "CheckWorstInputVaryNSparse"
etaPerformance = {}
etaPerformance[0.2] = {}
etaPerformance[0.3] = {}
etaPerformance[0.6] = {}
etaPerformance[0.8] = {}
def parse(fileName):
    global etaPerformance
    with open(fileName,'r',encoding='utf-8') as file:
        Lines = file.readlines()
        for line in Lines:
            nums = line.strip().split(",")
            eta = float(nums[2])
            N = int(nums[0])
            perf = float(nums[1])
            etaPerformance[eta][N] = perf


def plotPerformance(performance,eta):
    keys = sorted(list(performance.keys()))
    x = [int(el) for el in keys]
    y = [float(performance[el]) for el in keys ]
    print(keys)
    print(x)
    print(y)
    plt.plot(x, y)
    plt.title("Performance ratio vs N for reduction factor = "+str(eta)+" on sparse graphs")
    plt.show()
    plt.savefig(str(eta)+outName+".png", bbox_inches='tight')
    plt.clf()

def plotTiming(ilpTime, randomisedTime):
    keysIlp = sorted(list(ilpTime.keys()))
    xIlp = [int(el) for el in keysIlp]
    yIlp = [float(ilpTime[el]) for el in keysIlp]
    keysRandomised = sorted(list(randomisedTime.keys()))
    xRandomised = [int(el) for el in keysRandomised]
    yRandomised = [float(randomisedTime[el]) for el in keysRandomised]
    plt.plot(xIlp, yIlp, label="ILP solver time")
    plt.plot(xRandomised, yRandomised, label="Randomised solver time")
    plt.title("Running time comparison (worst case)")
    plt.legend()
    plt.show()
    plt.savefig('foo.png', bbox_inches='tight')

parse(fileName)
#print(etaPerformance[0.2])
#performance = {5: 1.0, 6: 2.0, 7: 2.0, 8: 2.0, 9: 2.0, 10: 2.0, 11: 3.0, 12: 2.0, 13: 2.0, 14: 2.0, 15: 2.0, 16: 2.0, 17: 2.0, 18: 2.0, 19: 2.0, 20: 2.0, 21: 2.0, 22: 2.0, 23: 3.0, 24: 2.0, 25: 3.0, 26: 2.0, 27: 3.0, 28: 2.0, 29: 2.0, 30: 3.0, 31: 3.0, 32: 3.0, 33: 2.0, 34: 3.0, 35: 3.0, 36: 5.0, 37: 2.0, 38: 3.0, 39: 2.0, 40: 4.0, 41: 4.0, 42: 3.0, 43: 6.0, 44: 4.0, 45: 4.0, 46: 7.0, 47: 3.0, 48: 5.0, 49: 6.0, 50: 6.0}
#ilpTime = {5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0, 25: 0.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.0, 31: 0.0, 32: 0.0, 33: 0.0, 34: 0.0, 35: 0.0, 36: 0.0, 37: 0.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 0.0, 42: 0.0, 43: 0.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 0.0, 49: 0.0, 50: 0.0}
#randomisedTime = {5: 0.0916292667388916, 6: 0.10260224342346191, 7: 0.08789587020874023, 8: 0.08303260803222656, 9: 0.11618256568908691, 10: 0.1112825870513916, 11: 0.11775493621826172, 12: 0.1158299446105957, 13: 0.1379852294921875, 14: 0.16757631301879883, 15: 0.2042069435119629, 16: 0.2289600372314453, 17: 0.23862314224243164, 18: 0.2785909175872803, 19: 0.3288302421569824, 20: 0.30410027503967285, 21: 0.40390610694885254, 22: 0.39988279342651367, 23: 0.44202423095703125, 24: 0.4955921173095703, 25: 0.5320494174957275, 26: 0.5901281833648682, 27: 1.3359506130218506, 28: 0.7026176452636719, 29: 0.8728005886077881, 30: 0.8932473659515381, 31: 0.9466700553894043, 32: 1.0115606784820557, 33: 1.1023037433624268, 34: 1.2106263637542725, 35: 1.3120968341827393, 36: 1.4135429859161377, 37: 1.852754831314087, 38: 2.0158791542053223, 39: 2.1339471340179443, 40: 2.518838882446289, 41: 2.3534739017486572, 42: 2.5510294437408447, 43: 2.8413124084472656, 44: 2.9399805068969727, 45: 3.169656753540039, 46: 3.3008527755737305, 47: 3.6800827980041504, 48: 3.786658525466919, 49: 3.9589381217956543, 50: 4.220818042755127}
plotPerformance(etaPerformance[0.2],0.2)
plotPerformance(etaPerformance[0.3],0.3)
plotPerformance(etaPerformance[0.6],0.6)
plotPerformance(etaPerformance[0.8],0.8)
#plotTiming(ilpTime, randomisedTime)

