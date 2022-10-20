from chromosome import Chromosome, to_number, to_binary
import random as rnd
import math

if __name__ == '__main__':
    population = []
    pop_size = 100
    answer = 870
    stop_threshold = 0.3
    max_generations = 100
    mutation_rate = 0.03

    # Create initial population with random values
    for i in range(pop_size):
        population.append(Chromosome(to_binary(rnd.randint(0, 45)),
                                     to_binary(rnd.randint(2, 5)),
                                     to_binary(rnd.randint(55, 75)/100),
                                     to_binary(rnd.randint(1000, 2000)),
                                     to_binary(rnd.randint(5, 50)/10),
                                     mutation_rate))

    average_population_fitness = float('inf')
    generation = 0

    # Loop until the average is close
    while average_population_fitness > stop_threshold and max_generations > generation:
        generation += 1
        pop_sum = 0

        for p in population:
            f = abs(p.eval() - answer)
            p.set_fitness(f)
            pop_sum += f

        average_population_fitness = pop_sum / len(population)

        population.sort(key=lambda x: x.get_fitness())

        print("Gen: {} Average population fitness: {} best individual: {}".format(generation,
                                                                                  average_population_fitness,
                                                                                  population[0]))
        # Choose roulette or elitist selection
        if bool(rnd.randint(0, 1)):
            # Roulette selection
            selection = []
            for j in range(pop_size):
                selection.append(math.log(pop_size-j))
            for k in range(pop_size):
                chosen_chromosomes = rnd.choices(population, weights=selection, k=2)
                match rnd.randint(0, 2):
                    case 0:
                        # Arithmetic crossover
                        new_offspring = chosen_chromosomes[0].arithmetic_crossover(chosen_chromosomes[1])
                    case 1:
                        # Single point crossover
                        new_offspring = chosen_chromosomes[0].single_point_crossover(chosen_chromosomes[1])
                    case 2:
                        # Multi point crossover
                        new_offspring = chosen_chromosomes[0].multi_point_crossover(chosen_chromosomes[1])
                    # Choose high or low level mutation
                new_offspring.high_level_mutate() if bool(rnd.randint(0, 1)) else new_offspring.low_level_mutate()
                population[k] = new_offspring
        else:
            # Elitist selection
            for j in range(1, int(pop_size/5) + 1):
                match rnd.randint(0, 2):
                    case 0:
                        # Arithmetic crossover
                        new_offspring = population[j - 1].arithmetic_crossover(population[j + 1])
                    case 1:
                        # Single point crossover
                        new_offspring = population[j - 1].single_point_crossover(population[j + 1])
                    case 2:
                        # Multi point crossover
                        new_offspring = population[j - 1].multi_point_crossover(population[j + 1])

                # Choose high or low level mutation
                new_offspring.high_level_mutate() if bool(rnd.randint(0, 1)) else new_offspring.low_level_mutate()
                population[len(population) - j] = new_offspring
