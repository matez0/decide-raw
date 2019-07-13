# coding: utf-8
#
# Copyright (c) 2019 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

class LinearDecider(object):
    def __init__(self, coefficients):
        """
        :param list coefficients: first item is for the original value, the others are for the values in time order
        """
        self.coefficients = coefficients[1:]
        # This makes easier to zip the coefficients and the input values, when there are less input values
        self.coefficients.reverse()
        self.coefficients.insert(0, coefficients[0])

    def eval(self, values):
        return sum((c * i for c, i in zip(self.coefficients, values)))

    def decide(self, orig_value, values):
        """
        :param int orig_value: the original value
        :param list values: values in time order, at most the last (len(self.coefficients) - 1) are used for calculation
        :return: True, if it is decided to choose the last value, otherwise False
        """
        values_to_eval = values[1 - len(self.coefficients):]
        values_to_eval.reverse()
        values_to_eval.insert(0, orig_value)
        return self.eval(values_to_eval) > 0

    def __repr__(self):
        return f'{self.__class__.__name__}({repr([self.coefficients[0]] + list(reversed(self.coefficients[1:])))})'
