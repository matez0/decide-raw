# coding: utf-8
#
# Copyright (c) 2021 Zoltán Máté
# All Rights Reserved.
#
# Author: Zoltán Máté <mate.zoltan0@gmail.com>
#

class CompositeDecider(object):
    def __init__(self, conjunction_of_disjunction_of_linear_deciders):
        """
        :param list conjunction_of_disjunction_of_linear_deciders: lists of linear deciders representing disjunctions
        """
        self.conjunction_of_disjunction_of_linear_deciders = conjunction_of_disjunction_of_linear_deciders

    def decide(self, orig_value, values):
        """
        :param int orig_value: the original value
        :param list values: values in time order, at most the last N values are used for calculation,
        where N is the maximum of the length of linear deciders.
        :return: True, if it is decided to choose the last value, otherwise False
        """
        return all(
            any(decider.decide(orig_value, values) for decider in disjunction_of_linear_deciders)
            for disjunction_of_linear_deciders in self.conjunction_of_disjunction_of_linear_deciders
        )

    def __repr__(self):
        return f'{self.__class__.__name__}({self.conjunction_of_disjunction_of_linear_deciders})'
