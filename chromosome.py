import random as rnd

mutation_rate = 0.05


def map_to_operator(val):
    match val:
        case 0:
            return '+'
        case 1:
            return '-'
        case 2:
            return '*'
        case 3:
            return '/'
        case _:
            return None


class Chromosome:
    def __init__(self, feature_1, feature_2, feature_3):
        self.feature_1 = feature_1  # [-1000, 1000]
        self.feature_2 = feature_2  # [-200, 200]
        self.feature_3 = feature_3  # [+, -, *, /]
        self.fitness = float('inf')

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness

    def get_fitness(self):
        return self.fitness

    def crossover(self, other):
        chance = bool(rnd.randint(0, 1))
        return Chromosome((self.feature_1 + other.feature_1) / 2,
                          (self.feature_2 + other.feature_2) / 2,
                          self.feature_3 if chance else other.feature_3)

    def mutate(self):
        chance = rnd.random()
        if chance < mutation_rate:
            self.feature_1 += rnd.randint(-100, 100)
            if self.feature_1 > 1000:
                self.feature_1 = 1000
            elif self.feature_1 < -1000:
                self.feature_1 = -1000

                self.feature_2 += rnd.randint(-30, 30)
            if self.feature_2 > 200:
                self.feature_2 = 200
            elif self.feature_2 < -200:
                self.feature_2 = -200

                self.feature_3 += rnd.randint(-2, 2)
            if self.feature_3 > 3:
                self.feature_3 = 3
            elif self.feature_3 < 0:
                self.feature_3 = 0

    def eval(self):
        if map_to_operator(self.feature_3) == '+':
            return self.feature_1 + self.feature_2
        if map_to_operator(self.feature_3) == '-':
            return self.feature_1 - self.feature_2
        if map_to_operator(self.feature_3) == '*':
            return self.feature_1 * self.feature_2
        if map_to_operator(self.feature_3) == '/':
            return self.feature_1 / self.feature_2
        else:
            return float('inf')

    def __str__(self):
        return "{} {} {} = {}".format(self.feature_1, map_to_operator(self.feature_3), self.feature_2, self.eval())
