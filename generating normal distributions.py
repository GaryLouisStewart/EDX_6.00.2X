import pylab
import scipy.integrate
import random
# the following below is an example from the lecture for generating distributions (should bring up a graph)

dist = []
for i in range(100000):
    dist.append(random.gauss(0, 30))
pylab.hist(dist, 30)

# checking the Empirical rule using the scipy library

def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian,
                                        mu-numStd*sigma,
                                        mu+numStd*sigma,
                                        (mu, sigma))[0]
            print(' Fraction within', numStd, 'std =', round(area, 4))
checkEmpirical(3)
