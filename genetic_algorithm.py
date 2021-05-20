from common import *
import sys

POPULATION_SIZE = 100

child_id = 0

class Individual:
    def __init__(self, chromosome):
        global child_id
        self.ID = child_id
        self.chromosome = chromosome
        self.weakness = numberOfIntersections(chromosome)
        child_id += 1

def offspring(firstParent, secondParent) -> Individual:
    childChromosome = []
    
    for i in range(len(firstParent.chromosome)):
        number = random.randint(0, 1)
            
        if number == 1: # add parts of first parent to child chromosome
            childChromosome.append(firstParent.chromosome[i])
        else:
            childChromosome.append(secondParent.chromosome[i])

    return Individual(childChromosome)
"""
def partition(temp_population, low, high):
    i = low - 1
    pivot = temp_population[high]
    
    sys.setrecursionlimit(10**6)

    for j in range(low, high):
        if temp_population[j].weakness <= pivot.weakness:
            i += i + 1
            temp_population[i], temp_population[j] = temp_population[j], temp_population[i]
    
    temp_population[i + 1], temp_population[high] = temp_population[high], temp_population[i + 1]
    return i + 1

def quickSort(temp_population, low, high):
    if len(temp_population) == 1:
        return
    
    if low < high:
        index = partition(temp_population, low, high)

        quickSort(temp_population, low, index - 1)
        quickSort(temp_population, index, high)
"""
"""
def bubbleSort(population):
    n = len(population)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
"""
def genetic_algorithm(state):
    global POPULATION_SIZE

    generation = 1
    solution = False
    population = []

    start_time = time.time()
    
    for _ in range(POPULATION_SIZE):
        population.append(Individual(chooseNewState(state)))
    
    file = open("genetic_algorithm_32x32", "w")
    
    while not solution:
        population = sorted(population, key = lambda x:x.weakness)

        if population[0].weakness == 0:
            solution = True
            break

        newPopulation = []

        # Survival of the fitted means only 15% will likely live
        newPopulation.extend(population[:POPULATION_SIZE * 15])

        # Reprsents the fact that males typcially mate with any amount of random female that are available
        size = 85 * POPULATION_SIZE
        for _ in range(size):
            firstParent = random.choice(population[:50])
            secondParent = random.choice(population[:50])
            child = offspring(firstParent, secondParent)
            newPopulation.append(child)
        
        population = newPopulation

        print("Generation: ", generation, " best child:", population[0].ID, " weakness: ", population[0].weakness)

        text = "Generation: " + str(generation) + " best child:" + str(population[0].ID) + " weakness: " + str(population[0].weakness)
        file.write(text + "\n")
        generation += 1

    end_time = time.time()
    
    print("Generation: ", generation, " child:", population[0].ID, "weakness: ", population[0].weakness)
    print("time span: ", end_time - start_time)
    return population[0]

if __name__ == '__main__':
    solution = genetic_algorithm(state32x32)
    printChessBoard(solution.chromosome)