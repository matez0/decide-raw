# coding: utf-8
#
# Copyright (c) 2021 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

import pytest
from unittest.mock import Mock

from composite_decider import CompositeDecider
from linear_decider import LinearDecider


def test_composite_decider_can_be_created_from_list_of_linear_decider_lists():
    assert CompositeDecider([
        [
            LinearDecider([1, 2, 3]),
            LinearDecider([4, 5, 6]),
        ],
        [
            LinearDecider([7, 8, 9]),
        ],
    ])


@pytest.mark.parametrize("decision_lists, expected", [
    ([[True]], True),
    ([[False]], False),
    ([[False, True]], True),
    ([[False, False]], False),
    ([[True], [False]], False),
    ([[True], [True]], True),
    ([[True, False], [False, True]], True),
])
def test_decide_returns_the_conjunction_of_disjunction_of_the_decision_of_linear_deciders(decision_lists, expected):
    decider_lists = [
        [Mock(**{'decide.return_value': decision}) for decision in decisions]
        for decisions in decision_lists
    ]
    assert CompositeDecider(decider_lists).decide(1, [2, 3]) is expected
