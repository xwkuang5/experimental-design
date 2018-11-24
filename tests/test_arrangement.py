import unittest

from . import context

from design.core import Design
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

        self.assertEqual(design._get_arrangement(), [
            ['phone::iphone', 'browser::safari'],
            ['phone::iphone', 'browser::chrome'],
            ['phone::iphone', 'browser::IE'],
            ['phone::huawei', 'browser::safari'],
            ['phone::huawei', 'browser::chrome'],
            ['phone::huawei', 'browser::IE'],
            ['phone::samsung', 'browser::safari'],
            ['phone::samsung', 'browser::chrome'],
            ['phone::samsung', 'browser::IE'],
        ])

    def test_within_subject_design(self):

        config = {
            'independentVariables': {
                'phone': {
                    'levels': ['iphone', 'huawei', 'samsung'],
                    'design': FactorType.between_subject.name
                },
                'browser': {
                    'levels': ['safari', 'chrome', 'IE'],
                    'design': FactorType.within_subject.name,
                    'order': OrderType.latin_square.name,
                }
            },
            'availableTasks': {
                'findPresidentOfUS': {
                    'repeatable': True
                }
            }
        }

        design = Design(config)

        self.assertEqual(design._get_arrangement(), [
            [
                'phone::iphone', [['browser::safari'], ['browser::chrome'],
                                  ['browser::IE']]
            ],
            [
                'phone::iphone', [['browser::chrome'], ['browser::IE'],
                                  ['browser::safari']]
            ],
            [
                'phone::iphone', [['browser::IE'], ['browser::safari'],
                                  ['browser::chrome']]
            ],
            [
                'phone::huawei', [['browser::safari'], ['browser::chrome'],
                                  ['browser::IE']]
            ],
            [
                'phone::huawei', [['browser::chrome'], ['browser::IE'],
                                  ['browser::safari']]
            ],
            [
                'phone::huawei', [['browser::IE'], ['browser::safari'],
                                  ['browser::chrome']]
            ],
            [
                'phone::samsung', [['browser::safari'], ['browser::chrome'],
                                   ['browser::IE']]
            ],
            [
                'phone::samsung', [['browser::chrome'], ['browser::IE'],
                                   ['browser::safari']]
            ],
            [
                'phone::samsung', [['browser::IE'], ['browser::safari'],
                                   ['browser::chrome']]
            ],
        ])
