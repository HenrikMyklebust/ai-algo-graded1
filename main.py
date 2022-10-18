from chromosome import Chromosome
import random as rnd

population = []
pop_size = 100
answer = 42
stop_threshold = 0.1

for i in range(pop_size):
    population.append(Chromosome(rnd.randint(-1000, 1000), rnd.randint(-200, 200), rnd.randint(0, 3)))

average_population_fitness = float('inf')

while average_population_fitness > stop_threshold:

    pop_sum = 0

    for p in population:
        f = abs(p.eval() - answer)
        p.set_fitness(f)
        pop_sum += f

    average_population_fitness = pop_sum / len(population)

    population.sort(key=lambda x: x.get_fitness())

    print("Average population fitness: {} best individual: {}".format(average_population_fitness, population[0]))

    for j in range(1, int(pop_size/5) + 1):
        new_offspring = population[j - 1].crossover(population[j + 1])
        new_offspring.mutate()
        population[len(population) - j] = new_offspring
