import random as rnd
import math


def to_binary(number):
    # 00000000000.0000000 to 11111010000.1100011
    if type(number) == float:
        num, decimal = str(number).split(".")

        if len(decimal) == 1:
            decimal = decimal + "0"

        num = bin(int(num))[2:]
        decimal = bin(int(decimal))[2:]

        difference = len("00000000000") - len(num)
        if difference > 0:
            num = "0" * difference + num

        difference = len("0000000") - len(decimal)
        if difference > 0:
            decimal = "0" * difference + decimal

        return "{}.{}".format(num, decimal)

    # 00000000000.0000000 to 11111010000.0000000
    elif type(number) == int:
        num = bin(int(number))[2:]

        while len(num) < len("00000000000"):
            num = "0" + num
        return "{}.0000000".format(num)


def to_number(binary):
    num, decimal = str(binary).split(".")

    # Return integer
    if decimal == "0000000":
        return int(num, 2)

    # Return float
    else:
        return float(str(int(num, 2)) + "." + str(int(decimal, 2)))


def change_bit(number):
    bit_index = rnd.randint(0, len(number) - 1)
    new_number = ""
    if number[bit_index] == '0':
        for i in range(len(number)):
            if i == bit_index:
                new_number = new_number + "1"
            else:
                new_number = new_number + number[i]
    else:
        for i in range(len(number)):
            if i == bit_index:
                new_number = new_number + "0"
            else:
                new_number = new_number + number[i]
    return new_number


class Chromosome:
    def __init__(self, feature_a, feature_b, feature_y, feature_d, feature_o, mutation_rate):
        # Binary format: 00000000000.0000000
        self.feature_a = feature_a  # Binary [0, 45]
        self.feature_b = feature_b  # Binary [2, 5]
        self.feature_y = feature_y  # Binary [0.55, 0.75]
        self.feature_d = feature_d  # Binary [1000, 2000]
        self.feature_o = feature_o  # Binary [0.5, 5.0]
        self.fitness = float('inf')
        self.mutation_rate = mutation_rate

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness

    def get_fitness(self):
        return self.fitness

    def arithmetic_crossover(self, other):
        return Chromosome(
            to_binary(int((to_number(self.feature_a) + to_number(other.feature_a)) / 2)),
            to_binary(int((to_number(self.feature_b) + to_number(other.feature_b)) / 2)),
            to_binary((to_number(self.feature_y) + to_number(other.feature_y)) / 2), # Should be float
            to_binary(int((to_number(self.feature_d) + to_number(other.feature_d)) / 2)),
            to_binary((to_number(self.feature_o) + to_number(other.feature_o)) / 2), # Should be float
            self.mutation_rate)

    def single_point_crossover(self, other):
        return Chromosome(
            self.feature_a if bool(rnd.randint(0, 1)) else other.feature_a,
            self.feature_b if bool(rnd.randint(0, 1)) else other.feature_b,
            self.feature_y if bool(rnd.randint(0, 1)) else other.feature_y,
            self.feature_d if bool(rnd.randint(0, 1)) else other.feature_d,
            self.feature_o if bool(rnd.randint(0, 1)) else other.feature_o,
            self.mutation_rate)

    def multi_point_crossover(self, other):
        feature_a, feature_b, feature_y, feature_d, feature_o = "", "", "", "", ""
        for i in range(len(self.feature_a)):
            feature_a = feature_a + self.feature_a[i] if bool(rnd.randint(0, 1)) else feature_a + other.feature_a[i]
            feature_b = feature_b + self.feature_b[i] if bool(rnd.randint(0, 1)) else feature_b + other.feature_b[i]
            feature_y = feature_y + self.feature_y[i] if bool(rnd.randint(0, 1)) else feature_y + other.feature_y[i]
            feature_d = feature_d + self.feature_d[i] if bool(rnd.randint(0, 1)) else feature_d + other.feature_d[i]
            feature_o = feature_o + self.feature_o[i] if bool(rnd.randint(0, 1)) else feature_o + other.feature_o[i]

        if feature_a > to_binary(45):
            feature_a = to_binary(45)
        elif feature_a < to_binary(0):
            feature_a = to_binary(0)

        if feature_b > to_binary(5):
            feature_b = to_binary(5)
        elif feature_b < to_binary(2):
            feature_b = to_binary(2)

        if feature_y > to_binary(0.75):
            feature_y = to_binary(0.75)
        elif feature_y < to_binary(0.55):
            feature_y = to_binary(0.55)

        if feature_d > to_binary(2000):
            feature_d = to_binary(2000)
        elif feature_d < to_binary(1000):
            feature_d = to_binary(1000)


        if feature_o > to_binary(5.0):
            feature_o = to_binary(5.0)
        elif feature_o < to_binary(0.5):
            feature_o = to_binary(0.5)

        return Chromosome(feature_a, feature_b, feature_y, feature_d, feature_o, self.mutation_rate)

    def high_level_mutate(self):
        chance = rnd.random()
        if chance < self.mutation_rate:
            self.feature_a = to_binary(to_number(self.feature_a) + rnd.randint(-5, 5))
            if self.feature_a > to_binary(45):
                self.feature_a = to_binary(45)
            elif self.feature_a < to_binary(0):
                self.feature_a = to_binary(0)

            self.feature_b = to_binary(to_number(self.feature_b) + rnd.randint(-2, 2))
            if self.feature_b > to_binary(5):
                self.feature_b = to_binary(5)
            elif self.feature_b < to_binary(2):
                self.feature_b = to_binary(2)

            self.feature_y = to_binary(to_number(self.feature_y) + (rnd.randint(-2, 2) / 100))
            if self.feature_y > to_binary(0.75):
                self.feature_y = to_binary(0.75)
            elif self.feature_y < to_binary(0.55):
                self.feature_y = to_binary(0.55)

            self.feature_d = to_binary(to_number(self.feature_d) + rnd.randint(-100, 100))
            if self.feature_d > to_binary(2000):
                self.feature_d = to_binary(2000)
            elif self.feature_d < to_binary(1000):
                self.feature_d = to_binary(1000)

            self.feature_o = to_binary(to_number(self.feature_o) + (rnd.randint(-5, 5) / 10))
            if self.feature_o > to_binary(5.0):
                self.feature_o = to_binary(5.0)
            elif self.feature_o < to_binary(0.5):
                self.feature_o = to_binary(0.5)

    def low_level_mutate(self):
        chance = rnd.random()
        if chance < self.mutation_rate:

            # Integer bit flip
            feature_a_num, feature_a_decimal = self.feature_a.split(".")
            feature_a_num = change_bit(feature_a_num)
            self.feature_a = feature_a_num + "." + feature_a_decimal
            if self.feature_a > to_binary(45):
                self.feature_a = to_binary(45)
            elif self.feature_a < to_binary(0):
                self.feature_a = to_binary(0)

            # Integer bit flip
            feature_b_num, feature_b_decimal = self.feature_b.split(".")
            feature_b_num = change_bit(feature_b_num)
            self.feature_b = feature_b_num + "." + feature_b_decimal
            if self.feature_b > to_binary(5):
                self.feature_b = to_binary(5)
            elif self.feature_b < to_binary(2):
                self.feature_b = to_binary(2)

            # Float bit flip
            feature_y_num, feature_y_decimal = self.feature_y.split(".")
            feature_y_decimal = change_bit(feature_y_decimal)
            self.feature_y = feature_y_num + "." + feature_y_decimal
            if self.feature_y > to_binary(0.75):
                self.feature_y = to_binary(0.75)
            elif self.feature_y < to_binary(0.55):
                self.feature_y = to_binary(0.55)

            # Integer bit flip
            feature_d_num, feature_d_decimal = self.feature_d.split(".")
            feature_d_num = change_bit(feature_d_num)
            self.feature_d = feature_d_num + "." + feature_d_decimal
            if self.feature_d > to_binary(2000):
                self.feature_d = to_binary(2000)
            elif self.feature_d < to_binary(1000):
                self.feature_d = to_binary(1000)

            # Float bit flip
            feature_o_num, feature_o_decimal = self.feature_o.split(".")
            feature_o_decimal = change_bit(feature_o_decimal)
            self.feature_o = feature_o_num + "." + feature_o_decimal
            if self.feature_o > to_binary(5.0):
                self.feature_o = to_binary(5.0)
            elif self.feature_o < to_binary(0.5):
                self.feature_o = to_binary(0.5)

    def eval(self):
        return (pow(to_number(self.feature_a), to_number(self.feature_b)) + math.log(to_number(self.feature_y))) / \
               (to_number(self.feature_d) + pow(to_number(self.feature_o), 3))

    def __str__(self):
        return "({}^{} + ln({:.2f})) / ({} + {:.2f}^3) = {:.3f}".format(to_number(self.feature_a),
                                                                        to_number(self.feature_b),
                                                                        to_number(self.feature_y),
                                                                        to_number(self.feature_d),
                                                                        to_number(self.feature_o),
                                                                        self.eval())
