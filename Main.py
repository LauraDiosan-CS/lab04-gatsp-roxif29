from GA import GA

def fitnessF(chromosome):
    repres = chromosome.repres
    g = chromosome.problParam['graph']
    fitness = 0.0
    for i in range(len(repres) - 1):
        fitness = fitness + g[repres[i]][repres[i-1]]
    return fitness


def readFromFileGraph(fileName):
    graph = []

    f = open(fileName, "r")
    dim = int(f.readline())

    for i in range(0, dim):
        line = f.readline()
        info = line.split(",")
        edge = []
        for j in range(0, dim):
            edge.append(int(info[j]))
        graph.append(edge)
    return graph
'''
def readFromFileGraphHard(fileName):
    graph = []

    f = open(fileName, "r")
    for _ in range(6):
        f.readline()
    line = f.readline()
    while (line) != "EOF":
    
    
    
    
    return graph'''


def main():
    graph = readFromFileGraph("easy1.txt")
    #graph = readFromFileGraphHard("hardE.txt")
    bestChromos = []
    genNo=200
    populationSize=100

    ga = GA(fitnessF,genNo,populationSize,graph,len(graph))
    ga.initialize()
    ga.evaluation()

    for i in range(genNo):
        ga.oneGenerationElitism()
        bestChromo = ga.bestChromo()
        bestChromos.append(bestChromo)

    print('best chromo: ' , str(bestChromo.repres) , '\n' , str(bestChromo.fitness))


main()