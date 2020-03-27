#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

import array
import random
import math

import numpy as np

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

def createIndividual():
    l = [0,0,0,0]
    return l
'''
creator.create("Fitness", base.Fitness, weights=(-1.0,))
#creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)
creator.create("Individual", list, fitness=creator.Fitness)
'''
# El objetivo es minimizar
creator.create("Fitness", base.Fitness, weights=(-1.0,))
# El individuo es una lista
creator.create("Individual", list, fitness=creator.Fitness)
toolbox = base.Toolbox()

# Attribute generator
#toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, createIndividual, 5)
#toolbox.register("individual", createIndividual)
#toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("population", tools.initRepeat, list, createIndividual)
def evalOneMax(individual):
    r = 0
    print("Individual: ",individual)
    return r,

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)

    pop = toolbox.population(n=20)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0, ngen=40,
                                   stats=stats, halloffame=hof, verbose=True)

    return pop, log, hof

if __name__ == "__main__":
    main()
