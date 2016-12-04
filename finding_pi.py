'''
Buffon-Laplace

As = 2*2 =4
Ac = Nr**2 = N (where N = Pi)

* (needles in circle/needles in square) / (area of circle/area of square)

* area of circle = (area of square * needles in circle)/ / (needles in square)

* area of circle = (4 * needles in circle) / (needles in square)

'''
import random

def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))


def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = getMeanAndStd(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(curEst) +\
          ', Std. dev. = ' + str(round(sDev, 6))\
          + ', Needles = ' + str(numNeedles))
    return (curEst, sDev)


def estPi(precision, numTrails):
    numNeedles = 100
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEst(numNeedles, numTrails)
        numNeedles *= 2
    return curEst