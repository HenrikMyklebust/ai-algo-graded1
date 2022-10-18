import random as rnd
import math


class Chromosome:
    def __init__(self, feature_a, feature_b, feature_y, feature_d, feature_o, mutation_rate):
        self.feature_a = feature_a  # [0, 45]
        self.feature_b = feature_b  # [2, 5]
        self.feature_y = feature_y  # [0.55, 0.75]
        self.feature_d = feature_d  # [1000, 2000]
        self.feature_o = feature_o  # [0.5, 5.0]
        self.fitness = float('inf')
        self.mutation_rate = mutation_rate

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness

    def get_fitness(self):
        return self.fitness

    def arithmetic_crossover(self, other):
        chance = bool(rnd.randint(0, 1))
        return Chromosome(
            (self.feature_a + other.feature_a) / 2,
            self.feature_b if chance else other.feature_b,
            (self.feature_y + other.feature_y) / 2,
            (self.feature_d + other.feature_d) / 2,
            (self.feature_o + other.feature_o) / 2,
            self.mutation_rate)

    def mutate(self):
        chance = rnd.random()
        if chance < self.mutation_rate:
            self.feature_a += rnd.randint(-5, 5)
            if self.feature_a > 45:
                self.feature_a = 45
            elif self.feature_a < 0:
                self.feature_a = 0

                self.feature_b += rnd.randint(-2, 2)
            if self.feature_b > 5:
                self.feature_b = 5
            elif self.feature_b < 2:
                self.feature_b = 2

                self.feature_y += rnd.uniform(-0.02, 0.02)
            if self.feature_y > 0.75:
                self.feature_y = 0.75
            elif self.feature_y < 0.55:
                self.feature_y = 0.55

                self.feature_d += rnd.randint(-100, 100)
            if self.feature_d > 2000:
                self.feature_d = 2000
            elif self.feature_d < 1000:
                self.feature_d = 1000

                self.feature_o += rnd.uniform(-0.5, 0.5)
            if self.feature_o > 5.0:
                self.feature_o = 5.0
            elif self.feature_o < 0.5:
                self.feature_o = 0.5

    def eval(self):
        return (pow(self.feature_a, self.feature_b) + math.log(self.feature_y)) / \
               (self.feature_d + pow(self.feature_o, 3))

    def __str__(self):
        return "({}^{} + ln({:.3f})) / ({} + {:.3f}^3) = {:.3f}".format(self.feature_a, self.feature_b, self.feature_y,
                                                                        self.feature_d, self.feature_o, eval())
