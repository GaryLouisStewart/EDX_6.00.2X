'''
the following is a simulation for the following problem...
** you have a bucket with 3 red balls and 3 green balls  **
    assume that once you draw a ball out of the bucket
    you don't replace it, what is the probability of drawing
     3 balls of the same color?

helper function is below...
'''
import random

def singleTrial():
    '''
    :return
    '''
    balls = ['r', 'r', 'r', 'g', 'g', 'g']
    ChoiceBalls = []
    for i in range(3):
        ball = random.choice(balls)
        balls.remove(ball)
        ChoiceBalls.append(ball)
    if ChoiceBalls[0] == ChoiceBalls[1] and ChoiceBalls[1] == ChoiceBalls[2]:
        return True
    return False

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''

    noTrue = 0
    for trial in range(numTrials):
        if singleTrial():
            noTrue += 1
    return float(noTrue)/float(numTrials)





