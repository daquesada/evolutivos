import array
import random
import math
import numpy as np
import readGraph as rg
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
graph = rg.buildGraph()
vertices = graph[0]
edges = graph[1]
adjacencyMatrix = graph[2]
def configurationToolBox(numGens):

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMin)
    toolbox = base.Toolbox()

    # Attribute generator
    toolbox.register("attr_bool", random.randint, 0, numGens-2)

    # Structure initializers
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool,numGens)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evalGraph)

    #options: cxOnePoint, cxTwoPoint, cxPartialyMatched, cxOrdered
    toolbox.register("mate", tools.cxTwoPoint)
    #toolbox.register("mate", tools.cxUniform, indpb=0.01)
    #toolbox.register("mate", tools.cxUniformPartialyMatched, indpb=0.01)


    #options: mutShuffleIndexes, mutFlipBit
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.001)
    #toolbox.register("mutate", tools.mutESLogNormal, c=4, indpb=0.5)
    #options: selTournament
    toolbox.register("select", tools.selTournament, tournsize=3)
    #toolbox.register("select", tools.selBest, k=2, tournsize=3)
    return toolbox
def numberColors(agent):
    unique_list = []
    # traverse for all elements
    for x in agent:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return len(unique_list)
def evalGraph(agent):
    penaltyRepeat = 0
    penaltyColors = 0
    numColors = numberColors(agent)
    numErrors = 0
    eval = 0
    i = 0
    while(i < len(adjacencyMatrix)):
        j = 0
        adjacencyColors = []
        while(j < len(adjacencyMatrix[i])):
            vertice = adjacencyMatrix[i][j]
            color = agent[vertice-1]
            if(color in adjacencyColors):
                #Color repeat
                #Penalty
                numErrors+=1
            adjacencyColors.append(color)
            j+=1
        i+=1
    #penalty for number of errors
    penaltyRepeat = (numErrors/(vertices-1)) * 100
    #Penalty for number of colors
    penaltyColors = (numColors/(vertices-1)) * 100
    eval = penaltyRepeat + penaltyColors
    return eval,
def main():
    random.seed(64)
    numGens = vertices
    toolbox = configurationToolBox(numGens)
    pop = toolbox.population(n=numGens*2)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=5000,
                                   stats=stats, halloffame=hof, verbose=True)

    e = numberColors(list(hof[0]))
    print("Solution: ",e)
    print(hof[0])

    return pop, log, hof

if __name__ == "__main__":
    main()
