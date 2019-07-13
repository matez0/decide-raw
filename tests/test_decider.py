# coding: utf-8
#
# Copyright (c) 2019 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

from decider import fitness, score
from linear_decider import LinearDecider


def test_score_1st_decision_of_comparator_decider():
    decider = LinearDecider([-1, 1])
    assert score(decider, [1, 1]) == 0
    assert score(decider, [9, 4]) == 0
    assert score(decider, [3, 9]) == 6
    assert score(decider, [2, 2, 2]) == 0
    assert score(decider, [1, 1, 3]) == 2
    assert score(decider, [1, 7, 1]) == 6
    assert score(decider, [2, 1, 1]) == 0
    assert score(decider, [1, 5, 9]) == 4


def test_score_1st_decision_of_on_decrease_decider():
    decider = LinearDecider([0, 1, -1])
    assert score(decider, [7, 2]) == 0
    assert score(decider, [1, 1, 1]) == 0
    assert score(decider, [1, 2, 3]) == 0
    assert score(decider, [1, 5, 9, 7, 3]) == 6


def test_score_1st_decision_of_binary_average_comparator_decider():
    decider = LinearDecider([-3, 1, 1, 1])
    assert score(decider, [1, 1]) == 0
    assert score(decider, [2, 2, 1]) == 0
    assert score(decider, [3, 3, 3]) == 0
    assert score(decider, [3, 3, 6]) == 0
    assert score(decider, [3, 3, 7]) == 4
    assert score(decider, [4, 4, 4, 9]) == 5


def test_fitness_of_comaprator_decider():
    decider = LinearDecider([-1, 1])
    assert fitness(decider, [1, 2, 3, 4, 5]) == 1 + 1 + 1 + 1
    assert fitness(decider, [4, 1, 2, 3, 4, 5, 7, 9]) == 1 + 1 + 1 + 1 + 1 + 2 + 2
    assert fitness(decider, [4, 3, 2, 5, 4, 5]) == 1 + 2 + 3 + 1
