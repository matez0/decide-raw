# coding: utf-8
#
# Copyright (c) 2021 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

"""
Application for evolving fixed size composite deciders
"""

import matplotlib.pyplot as plt
import random

from composite_decider import CompositeDecider
import data
from decider import fitness
from evolver import Evolver
from linear_decider import LinearDecider
from linear_decider_evolver_app import fitnesses, plot_fitness_distributions, print_population


linear_decider_size = 3
disjunction_size = 3
conjunction_size = 2

mutation_rate = 20
iteration = 40
population_size = 20

random.seed(0)


class SubEntity(LinearDecider):
    def breed(self):
        return type(self)([
            coefficient + random.randint(-mutation_rate, mutation_rate)
            for coefficient in self.coefficients
        ])


class Entity(CompositeDecider):
    __slots__ = 'fitness',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fitness = fitness(self, data.values)

    def breed(self):
        return type(self)([
            [sub_entity.breed() for sub_entity in disjunction_of_linear_deciders]
            for disjunction_of_linear_deciders in self.conjunction_of_disjunction_of_linear_deciders
        ])


def create_initial_population():
    return [
        Entity([
            [
                SubEntity(coefficients=[
                    random.randint(-linear_decider_size, linear_decider_size)
                    for idx in range(linear_decider_size)
                ])
                for idx in range(disjunction_size)
            ]
            for idx in range(conjunction_size)
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

        plot_fitness_distributions(fitness_evolution)

        plt.show()


if __name__ == '__main__':
    main()
