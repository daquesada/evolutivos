import numpy as np

def shannonEntropy(individuals):
    """
    :param individual: to calculate the fitness
    :var fitnessList: is a fitness list from the population
    :var size_fitness: is the size form the fitness list 
    :var repeatCount:  how many times a valor repeats in the fitness list
    :var probability: list to be chosen 
    :var size_probability: size form the probability list
    :returns: The shannon entropy, How diverse is the population
    """
    fitnessList = getIndividualsFitness(individuals)
    size_fitness = len(fitnessList)
    repeatCount = np.bincount(fitnessList)
    probability = repeatCount[np.nonzero(repeatCount)]/size_fitness
    size_probability = len(probability)
    if size_probability <= 1:
        return 0
    return - np.sum(probability * np.log(probability)) /np.log(size_probability)

def getIndividualsFitness(individuals):
    """To Do, Get the real fitness"""
    """Append in a list and return that list"""
    return [50,50,3,4,5,6,50,50,50,50,50,50,50,50,50,50,\
    50,50,50,50,50,3000,4,5,6,50,50,50,50,50,50,50,50,50,50,50,50,50]

individuals = [[],[],[],[]]
print(shannonEntropy(individuals))
