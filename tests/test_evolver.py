# coding: utf-8
#
# Copyright (c) 2019 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

from unittest.mock import Mock

from evolver import Evolver


def test_evolve_empty_population_gives_empty_one():
    assert Evolver.evolve([]) == []


class EntityBreadingWithOffspringSuffix(str):
    def breed(self):
        return type(self)(self + "offspring")


def test_breed_population_gives_the_breed_of_each_entity():
    Entity = EntityBreadingWithOffspringSuffix
    new_population = Evolver.breed([Entity("one"), Entity("other")])
    assert "oneoffspring" in new_population
    assert "otheroffspring" in new_population
    assert len(new_population) == 2


def test_sort_by_fitness_gives_entities_descending_order_by_fitness():
    entity_1 = Mock(fitness=1)
    entity_2 = Mock(fitness=2)
    entity_3 = Mock(fitness=3)
    population = Evolver.sort_by_fitness([entity_1, entity_3, entity_2])
    assert population == [entity_3, entity_2, entity_1]
    assert [entity.fitness for entity in population] == [3, 2, 1]


def test_select_high_fitness_entities_gives_the_first_half_of_the_population():
    Entity = Mock
    first_half = [Entity(), Entity(), Entity()]
    second_half = [Entity(), Entity(), Entity()]
    assert first_half != second_half
    assert Evolver.select_high_fitness_entities(first_half + second_half) == first_half


class EntityBreadingOffspringWithDoubleFitness(int):
    def __init__(self, fitness):
        self.fitness = fitness

    def breed(self):
        return type(self)(self.fitness * 2)


def test_evolve_gives_population_with_greater_fitness_sorted_by_fitness():
    Entity = EntityBreadingOffspringWithDoubleFitness
    assert Evolver.evolve([Entity(-1), Entity(-3), Entity(3)]) == [Entity(6), Entity(3), Entity(-1)]
