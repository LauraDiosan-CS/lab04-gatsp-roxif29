from random import randint

from Chromosome import Chromosome

class GA:
    def __init__(self, fitnessF,genNo,populationSize,graph,nodesNo):
        self.__population = []
        self.__fitnessF = fitnessF
        self.__genNo = genNo
        self.__populationSize = populationSize
        self.__graph = graph
        self.__nodesNo = nodesNo


    @property
    def population(self):
        return self.__population

    def initialize(self):
        problParam={"noNodes": self.__nodesNo, "graph": self.__graph}
        for i in range(0, self.__populationSize):
            c = Chromosome(problParam)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__fitnessF(c)

    def bestChromo(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def worstChromo(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__populationSize - 1)
        pos2 = randint(0, self.__populationSize - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__populationSize):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromo()]
        for _ in range(self.__populationSize - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__populationSize):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__fitnessF(off.repres,self.__graph)
            worst = self.worstChromo()
            if off.fitness < worst.fitness:
                worst = off