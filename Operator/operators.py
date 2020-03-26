import random

def cxTwoPoint(ind1, ind2):
    size = min(len(ind1), len(ind2))
    cxpoint1 = random.randint(1, size)
    cxpoint2 = random.randint(1, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1
    print(cxpoint1," ",cxpoint2)
    ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] = ind2[cxpoint1:cxpoint2], ind1[cxpoint1:cxpoint2]

    return ind1, ind2

'''
:k: probabilidad
'''

def selTournament(individuals, tournsize, k):
    chosen= []
    for _ in range(k):

        aspirants = selRandom(individuals, tournsize)
        #chosen.append((aspirants))

    return chosen

def selRandom(individuals,k):
    return [random.choice(individuals) for i in range(k)]


''''
l1=[0,1,0,0,1]
l2=[1,0,0,0,0]
aspirants = [l1.append(1),l2.append(2),[4,1,2,3,5],[6,7,8,9,0]]

print(selTournament(aspirants, 2, 3))
def selBest(individuals):
    best = []
    best = [evalGraph(individuals) for i in range (len(individuals))]
    return []
''''