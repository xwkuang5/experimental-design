import unittest
from itertools import product

from . import context

from design.core import Design
from design.parser import parse_config
from design.factors import Factor, FactorType, OrderType

class TestParticipantCalculation(unittest.TestCase):

    def test_between_subject_design(self):

        config = {
            'independentVariables': {
                'phone': {
                    'levels': ['iphone', 'huawei', 'samsung'],
                    'design': FactorType.between_subject.name
                },
                'browser': {
                    'levels': ['safari', 'chrome', 'IE'],
                    'design': FactorType.between_subject.name
                }
            },
            'availableTasks': {
                'findPresidentOfUS': {
                    'repeatable': True
                }
            }
        }

        design = Design(config)

        self.assertEqual(design.get_min_num_participants(), 9)

    def test_within_subject_design(self):

        config = {
            'independentVariables': {
                'phone': {
                    'levels': ['iphone', 'huawei', 'samsung'],
                    'design': FactorType.within_subject.name,
                    'order': None,
                },
                'browser': {
                    'levels': ['safari', 'chrome', 'IE'],
                    'design': FactorType.within_subject.name,
                    'order': None
                }
            },
            'availableTasks': {
                'findPresidentOfUS': {
                    'repeatable': True
                }
            }
        }

        order_list = [order.name for order in OrderType]
        answers = [1, 3, 6, 6]

        for i, (order_pair, answer_pair) in enumerate(zip(product(order_list, repeat=2), product(answers, repeat=2))):
            with self.subTest(i=i):
                config['independentVariables']['phone']['order'] = order_pair[0]
                config['independentVariables']['browser']['order'] = order_pair[1]
                design = Design(config)
                self.assertEqual(design.get_min_num_participants(), answer_pair[0] * answer_pair[1])

    def test_mixed_design(self):

        config = {
            'independentVariables': {
                'phone': {
                    'levels': ['iphone', 'huawei', 'samsung'],
                    'design': FactorType.between_subject.name,
                },
                'browser': {
                    'levels': ['safari', 'chrome', 'IE'],
                    'design': FactorType.within_subject.name,
                    'order': None
                }
            },
            'availableTasks': {
                'findPresidentOfUS': {
                    'repeatable': True
                }
            }
        }

        order_list = [order.name for order in OrderType]
        answers = [3, 9, 18, 18]

        for i, (order, answer) in enumerate(zip(order_list, answers)):
            with self.subTest(i=i):
                config['independentVariables']['browser']['order'] = order
                design = Design(config)
                self.assertEqual(design.get_min_num_participants(), answer)