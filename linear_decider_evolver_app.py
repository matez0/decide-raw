# coding: utf-8
#
# Copyright (c) 2021 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

"""
Application for evolving fixed size linear deciders
"""

import matplotlib.pyplot as plt
import random

import data
from decider import fitness
from evolver import Evolver
from linear_decider import LinearDecider

decider_size = 3

mutation_rate = 20
iteration = 40
population_size = 20

random.seed(0)


class Entity(LinearDecider):
    __slots__ = 'fitness',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fitness = fitness(self, data.values)

    def breed(self):
        return Entity([
            coefficient + random.randint(-mutation_rate, mutation_rate)
            for coefficient in self.coefficients
        ])


def print_population(population):
    print("population = [\n    {}\n]".format(",\n    ".join([repr(entity) for entity in population])))


def fitnesses(population):
    return [entity.fitness for entity in population]


def plot_fitness_distributions(fitness_evolution):
    for iteration_count, yvalues in fitness_evolution:
        plt.step(range(len(yvalues)), yvalues, label=iteration_count, where='post')
    plt.xlabel('rank of decider')
    plt.ylabel('fitness')
    plt.title('Distribution of fitness after given iteratation')
    plt.legend()


def plot_coefficients_by_fitness(population):
    for idx, (label, entity) in enumerate(zip(['most fit', 'medium', 'least'], population[::len(population) // 2 - 1])):
        plt.bar([(idx - 1) / 4 + x for x in range(len(entity.coefficients))], entity.coefficients, 1 / 4, label=label)
    plt.xlabel('coefficient index')
    plt.ylabel('coefficient value')
    plt.title('Coefficients by fitness')
    plt.xticks(range(decider_size))
    plt.grid(axis='x')
    plt.legend()


def create_initial_population():
    return [
        Entity(coefficients=[
            random.randint(-decider_size, decider_size)
            for idx in range(decider_size)
        ])
        for idx in range(population_size)
    ]


def main():
    population = create_initial_population()

    population = Evolver.sort_by_fitness(population)

    print('Initial population:')
    print_population(population)

    fitness_evolution = [(0, fitnesses(population))]

    try:
        for n in range(iteration):
            population = Evolver.evolve(population)

            print(n, fitnesses(population), end="    \r")

            if (n + 1) % (iteration // 4) == 0:
                fitness_evolution += [(n + 1, fitnesses(population))]

    except KeyboardInterrupt:
        pass

    finally:
        print('Final population:')
        print_population(population)

        plt.subplot(1, 2, 1)
        plot_fitness_distributions(fitness_evolution)

        plt.subplot(1, 2, 2)
        plot_coefficients_by_fitness(population)

        plt.show()


if __name__ == '__main__':
    main()
