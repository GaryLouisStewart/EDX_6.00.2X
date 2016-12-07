# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import random
import pylab

'''
Begin helper code
'''


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


'''
End helper code
'''


#
# PROBLEM 1
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        if self.clearProb > random.random():
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        if (self.getMaxBirthProb() * (1 - popDensity)) > random.random():
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop
        self.densePop = len(self.viruses) / float(self.maxPop)

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses[:]

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """
        for virus in self.viruses[:]:
            if virus.doesClear():
                self.viruses.remove(virus)
        self.densePop = len(self.viruses) / float(self.getMaxPop())

        if self.densePop <= 1:
            for virus in self.viruses[:]:
                try:
                    self.viruses.append(virus.reproduce(self.densePop))
                except NoChildException:
                    pass
        return len(self.viruses)


# viruses = [SimpleVirus(0.34, 0.94), SimpleVirus(0.57, 0.77), SimpleVirus(0.51, 0.06), SimpleVirus(0.59, 0.46),
#            SimpleVirus(0.05, 0.2)]
# P1 = Patient(viruses, 7)
# print(P1.getTotalPop())
# virus = SimpleVirus(1.0, 0.0)
# patient = Patient([virus], 100)
# print(patient.update())
# print(patient.update())
# print(patient.update())
# print(patient.update())
# print(patient.update())
# print(patient.update())
# print(patient.update())
# print(patient.update())
# print(patient.getTotalPop())
# virus = SimpleVirus(1.0, 1.0)
# patient = Patient([virus], 100)
# print(patient.getTotalPop())
# viruses = [SimpleVirus(0.46, 0.95), SimpleVirus(0.74, 0.72), SimpleVirus(0.39, 0.72)]
# P1 = Patient(viruses, 9)
# print(P1.getTotalPop())


#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    vList = [0] * 300
    for sim in range(numTrials):
        viruses = []
        for virus in range(numViruses):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))

        virusPop = []
        patient = Patient(viruses, maxPop)
        for i in range(300):
            patient.update()
            virusPop.append(patient.getTotalPop())
            vList[i] += patient.getTotalPop()

    avgVirusList= [x / float(numTrials) for x in vList]

    pylab.title('Average population of virus in patient')
    pylab.xlabel('Time steps')
    pylab.ylabel('Average virus population')
    pylab.plot(avgVirusList, label = 'Viruses')
    pylab.legend()
    pylab.show()

simulationWithoutDrug(100, 1000, 0.99, 0.05, 2)
simulationWithoutDrug(100, 1000, 0.1, 0.99, 2)
simulationWithoutDrug(100, 600, 0.77, 0.03, 3)


