# coding: utf-8
#
# Copyright (c) 2019 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

def score(decider, values):
    future_values = list(values)
    orig_value = future_values.pop(0)
    past_values = []
    while future_values:
        past_values.append(future_values.pop(0))
        if decider.decide(orig_value, past_values):
            return past_values[-1] - orig_value
    return 0


def fitness(decider, values):
    return sum((score(decider, values[orig:]) for orig in range(0, len(values))))
