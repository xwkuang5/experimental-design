import unittest

from . import context

from design.parser import parse_config
from design.factors import Factor, FactorType, OrderType


class TestParser(unittest.TestCase):
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
        }

        parsed_config = parse_config(config)

        self.assertDictEqual(
            parsed_config, {
                FactorType.between_subject.name: [
                    Factor('phone', ['iphone', 'huawei', 'samsung'],
                           FactorType.between_subject.name),
                    Factor('browser', ['safari', 'chrome', 'IE'],
                           FactorType.between_subject.name),
                ],
            })

    def test_within_subject_design(self):

        config = {
            'independentVariables': {
                'phone': {
                    'levels': ['iphone', 'huawei', 'samsung'],
                    'order': OrderType.sequential.name,
                    'design': FactorType.within_subject.name
                },
                'browser': {
                    'levels': ['safari', 'chrome', 'IE'],
                    'order': OrderType.sequential.name,
                    'design': FactorType.within_subject.name
                }
            },
        }

        parsed_config = parse_config(config)

        self.assertDictEqual(
            parsed_config, {
                FactorType.within_subject.name: [
                    Factor('phone', ['iphone', 'huawei', 'samsung'],
                           FactorType.within_subject.name,
                           OrderType.sequential.name),
                    Factor('browser', ['safari', 'chrome', 'IE'],
                           FactorType.within_subject.name,
                           OrderType.sequential.name),
                ],
            })

    def test_mixed_design(self):
        config = {
            'independentVariables': {
                'phone': {
                    'levels': ['iphone', 'huawei', 'samsung'],
                    'design': FactorType.between_subject.name
                },
                'browser': {
                    'levels': ['safari', 'chrome', 'IE'],
                    'order': OrderType.sequential.name,
                    'design': FactorType.within_subject.name
                }
            },
        }

        parsed_config = parse_config(config)

        self.assertDictEqual(
            parsed_config, {
                FactorType.between_subject.name: [
                    Factor('phone', ['iphone', 'huawei', 'samsung'],
                           FactorType.between_subject.name),
                ],
                FactorType.within_subject.name: [
                    Factor('browser', ['safari', 'chrome', 'IE'],
                           FactorType.within_subject.name,
                           OrderType.sequential.name),
                ],
            })
