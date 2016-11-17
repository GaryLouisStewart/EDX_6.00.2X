###################
# a simple example below
#
import pylab as plt


def pylab_example(b):
    """
    :rtype: graph plot
    :param
    return an example plot
    """
    genSamples = []
    genLinear = []
    genQuadratic = []
    genCubic = []
    genExponential = []

    for i in range(0, 30):
        genSamples.append(i)
        genLinear.append(i)
        genQuadratic.append(i ** 2)
        genCubic.append(i ** 3)
        genExponential.append(1.5 ** i)

    if b == 1:
        return plt.plot(genSamples, genLinear)
    elif b == 2:
        return plt.plot(genSamples, genQuadratic)
    elif b == 3:
        return plt.plot(genSamples, genCubic)
    elif b == 4:
        return plt.plot(genSamples, genExponential)
    else:
        if b == 5:
            return plt.plot(genExponential, genQuadratic, genCubic, genExponential)


pylab_example(5)


def multi_graph(c):
    """

    :param c can be any number
    return multiple graphs compared that are not overlaid
    """
    genSamples = []
    genLinear = []
    genQuadratic = []
    genCubic = []
    genExponential = []

    for i in range(0, 30):
        genSamples.append(i)
        genLinear.append(i)
        genQuadratic.append(i ** 2)
        genCubic.append(i ** 3)
        genExponential.append(1.5 ** i)

    if c == 1:
        return plt.figure('lin')
        return plt.plot(genSamples, genLinear)
    elif c == 2:
        return plt.figure('expo')
        return plt.plot(genSamples, genExponential)


multi_graph(1)
multi_graph(2)



