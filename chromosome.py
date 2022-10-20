import random as rnd
import math


def to_binary(number):
    # 00000000000.0000000 to 11111010000.1100011
    if type(number) == float:
        return

    elif type(number) == int:
        return
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
        return Chromosome(
            bin(int((int(self.feature_a) + int(other.feature_a)) / 2)),
            bin(int((int(self.feature_b) + int(other.feature_b)) / 2)),
            bin(int((int(self.feature_y) + int(other.feature_y)) / 2)), # Should be float
            bin(int((int(self.feature_d) + int(other.feature_d)) / 2)),
            bin(int((int(self.feature_o) + int(other.feature_o)) / 2)), # Should be float
            self.mutation_rate)

    def single_point_crossover(self, other):
        return Chromosome(
            self.feature_a if bool(rnd.randint(0, 1)) else other.feature_a,
            self.feature_b if bool(rnd.randint(0, 1)) else other.feature_b,
            self.feature_y if bool(rnd.randint(0, 1)) else other.feature_y,
            self.feature_d if bool(rnd.randint(0, 1)) else other.feature_d,
            self.feature_o if bool(rnd.randint(0, 1)) else other.feature_o,
            self.mutation_rate)

    #def multi_point_crossover(self, other):
    #    return Chromosome(
    #        self.feature_a if bool(rnd.randint(0, 1)) else other.feature_a,
    #        self.feature_b if bool(rnd.randint(0, 1)) else other.feature_b,
    #        self.feature_y if bool(rnd.randint(0, 1)) else other.feature_y,
    #        self.feature_d if bool(rnd.randint(0, 1)) else other.feature_d,
    #        self.feature_o if bool(rnd.randint(0, 1)) else other.feature_o,
    #        self.mutation_rate)

    def mutate(self):
        chance = rnd.random()
        if chance < self.mutation_rate:
            self.feature_a = bin(int(self.feature_a, 2) + rnd.randint(-5, 5))
            if self.feature_a > bin(45):
                self.feature_a = bin(45)
            elif self.feature_a < bin(0):
                self.feature_a = bin(0)

            self.feature_b = bin(int(self.feature_b, 2) + rnd.randint(-2, 2))
            if self.feature_b > bin(5):
                self.feature_b = bin(5)
            elif self.feature_b < bin(2):
                self.feature_b = bin(2)

            self.feature_y += rnd.uniform(-0.02, 0.02)
            if self.feature_y > 0.75:
                self.feature_y = 0.75
            elif self.feature_y < 0.55:
                self.feature_y = 0.55

            self.feature_d = bin(int(self.feature_d, 2) + rnd.randint(-100, 100))
            if self.feature_d > bin(2000):
                self.feature_d = bin(2000)
            elif self.feature_d < bin(1000):
                self.feature_d = bin(1000)

            self.feature_o += rnd.uniform(-0.5, 0.5)
            if self.feature_o > 5.0:
                self.feature_o = 5.0
            elif self.feature_o < 0.5:
                self.feature_o = 0.5

    def eval(self):
        return (pow(int(self.feature_a, 2), int(self.feature_b, 2)) + math.log(int(self.feature_y, 2))) / \
               (int(self.feature_d, 2) + pow(int(self.feature_o, 2), 3))

    def __str__(self):
        return "({}^{} + ln({:.3f})) / ({} + {:.3f}^3) = {:.3f}".format(self.feature_a, self.feature_b, self.feature_y,
                                                                        self.feature_d, self.feature_o, eval())
