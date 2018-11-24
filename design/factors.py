import math
import enum

import itertools

from helpers import construct_latin_square


class FactorType(enum.IntEnum):
    between_subject = 0
    within_subject = 1


class OrderType(enum.IntEnum):
    sequential = 0
    latin_square = 1
    balanced_latin_square = 2
    fully_counter_balanced = 3


class Factor:
    def __init__(self, name, levels, design, order=None):

        self.var = name
        self.card = len(levels)
        self.val = [name + '::' + level for level in levels]
        self.design = design
        self.order = order

    def __repr__(self):

        return "\nName: {}\nCard: {}\nVal: {}\nDesign: {}\nOrder: {}\n".format(
            self.var, self.card, "-".join(self.val), self.design, self.order)

    def __eq__(self, other):

        return self.__repr__() == other.__repr__()

    def get_multiplier(self):

        if self.design == FactorType.between_subject.name:
            return self.card
        elif self.design == FactorType.within_subject.name:
            if self.order == OrderType.sequential.name:
                return 1
            elif self.order == OrderType.latin_square.name:
                return self.card
            elif self.order == OrderType.balanced_latin_square.name:
                return self.card if self.card % 2 == 0 else self.card * 2
            elif self.order == OrderType.fully_counter_balanced.name:
                return math.factorial(self.card)

    def get_conditions(self):

        if self.design == FactorType.between_subject.name:
            return self.val
        elif self.design == FactorType.within_subject.name:
            if self.order == OrderType.sequential.name:
                return [self.val]
            elif self.order == OrderType.latin_square.name:
                return construct_latin_square(
                    self.val, balanced=False, randomized=False)
            elif self.order == OrderType.balanced_latin_square.name:
                return construct_latin_square(
                    self.val, balanced=True, randomized=False)
            elif self.order == OrderType.fully_counter_balanced.name:
                return list(itertools.permutations(self.val))
            else:
                raise ValueError('Order type {} not yet supported!'.format(
                    self.order))
