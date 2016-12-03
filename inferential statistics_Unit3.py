import statistics

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    n = len(L)
    if len(L) == 0:
        return float('NaN')
    lengths = [len(item) for item in L]
    return(statistics.pstdev(lengths))

# using listcomps to solve the problem

def stdDevOfLengths1(M):
    """

    :M a list of strings
    returns: float, the standard deviation of the lengths of the strings,
    or NaN if M is empty
    """

    n = len(M)
    if (n == 0):
        return float('NaN')
    lengths     = [len(s) for s in M]
    mean        = sum(lengths) / n
    squaredDev  = [(m-mean)**2 for m in lengths]
    variance    = sum(squaredDev) / n
    return variance**(.5)

# using a separate function for standard deviation

def stdDev(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def stdDevOfLengths2(N):
    n = len(N)
    if (n == 0):
        return float('NaN')
    X = []
    for s in N:
        X.append(len(s))
    return stdDev(X)