# coding: utf-8
#
# Copyright (c) 2019 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

from linear_decider import LinearDecider


def test_create_decider():
    assert LinearDecider([1, 2, 3])


def test_decider_evaluate_linear_combination_of_reversed_values_starting_with_orig():
    decider = LinearDecider([5, 2, 7])
    assert decider.eval([10, 100, 1000]) == 5 * 10 + 2 * 1000 + 7 * 100


def test_comparator_decider_decide_on_greater_than_origin():
    decider = LinearDecider([-1, 1])
    assert decider.decide(7, [9])
    assert decider.decide(5, [4, 6])
    assert decider.decide(6, [7, 9])
    assert decider.decide(5, [1, 2, 3, 8])
    assert decider.decide(3, [2]) is False
    assert decider.decide(5, [5]) is False
    assert decider.decide(5, [9, 5]) is False
    assert decider.decide(5, [7, 4]) is False
    assert decider.decide(4, [7, 9, 2]) is False


def test_on_decrease_decider_decide_on_decrease():
    decider = LinearDecider([0, 1, -1])
    assert decider.decide(3, [1, 2, 3, 4, 3])
    assert decider.decide(5, [4, 6]) is False
    assert decider.decide(5, [4, 4, 4, 4]) is False
