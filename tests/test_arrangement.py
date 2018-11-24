import unittest

from . import context

from itertools import product

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

        self.assertEqual(design.get_arrangement(), [
            ['iphone', 'safari'],
            ['iphone', 'chrome'],
            ['iphone', 'IE'],
            ['huawei', 'safari'],
            ['huawei', 'chrome'],
            ['huawei', 'IE'],
            ['samsung', 'safari'],
            ['samsung', 'chrome'],
            ['samsung', 'IE'],
        ])