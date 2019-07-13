# coding: utf-8
#
# Copyright (c) 2019 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

"""
Simple evolutionary algorithm with asexual breeding
"""

from multiprocessing import Pool


class Evolver(object):
    @classmethod
    def evolve(cls, population):
        population += cls.breed(population)
        population_sorted_by_fitness = cls.sort_by_fitness(population)
        return cls.select_high_fitness_entities(population_sorted_by_fitness)

    @staticmethod
    def breed(population):
        with Pool() as pool:
            return pool.map(breed, population)

    @staticmethod
    def sort_by_fitness(population):
        return sorted(population, key=lambda x: x.fitness, reverse=True)

    @staticmethod
    def select_high_fitness_entities(population):
        return population[:len(population) >> 1]


def breed(entity):
    return entity.breed()
