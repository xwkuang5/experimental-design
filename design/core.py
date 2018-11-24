from functools import reduce
from itertools import product

from parser import parse_config
from factors import Factor, FactorType, OrderType


class Design:
    def __init__(self, config):
        """Initialize a design instance with a condiguration object

        Args:
            config (object): JSON configuration of the experimental design
        """

        parsed_config = parse_config(config)

        self.between_subject_factors = parsed_config.get(
            FactorType.between_subject.name, [])
        self.within_subject_factors = parsed_config.get(
            FactorType.within_subject.name, [])
        self.tasks = parsed_config['tasks']

    def get_experimental_design(self):
        """Return the parsed experimental design as a JSON object

        Returns:
            config (object): parsed experimental design
        """

        return {
            'minimumNumberOfParticipants':
            self._get_min_num_participants(),
            'numberOfConditionsPerParticipant':
            self._get_num_conditions_per_participant(),
            'arrangements':
            self._get_arrangement()
        }

    def _get_arrangement(self):
        """Return all possible arrangements of experimental conditions

        Returns:
            list: A list of all possible arrangement of experimental conditions

        Examples:
            Assume two between-subject factors A and B and two within-subject factors C and D, each with two levels, the
            `get_arrangement` function returns the following:
            [
                [
                    between-subject-factorA-level1,
                    between-subject-factorB-level1,
                    [
                        [
                            [within-subject-factorC-level1, within-subject-factorD-level1],
                            [within-subject-factorC-level2, within-subject-factorD-level2]
                        ],
                        [
                            [within-subject-factorC-level2, within-subject-factorD-level1],
                            [within-subject-factorC-level1, within-subject-factorD-level2]
                        ],
                        [
                            [within-subject-factorC-level1, within-subject-factorD-level2],
                            [within-subject-factorC-level2, within-subject-factorD-level1]
                        ],
                        [
                            [within-subject-factorC-level2, within-subject-factorD-level2],
                            [within-subject-factorC-level1, within-subject-factorD-level1]
                        ],
                    ]
                ],
                [
                    between-subject-factorA-level1,
                    between-subject-factorB-level2,
                    [
                        ...
                    ]
                ]
            ]
        """

        conditions_list = []
        if len(self.between_subject_factors) != 0:
            conditions_list += [
                factor.get_conditions()
                for factor in self.between_subject_factors
            ]
        if len(self.within_subject_factors) != 0:
            conditions_list += [self._get_participant_conditions()]

        return [list(combination) for combination in product(*conditions_list)]

    def _get_participant_conditions(self):
        """Return all possible arragements of within-subjects conditions

        Returns:
            list: A list of all possible arragements of within-subject conditions

        Examples:
            Assume two within-subject factors A and B, each with two levels, the `_get_participant_conditions` function
            returns the following:
                [
                    [
                        [factorALevel1, factorBLevel1], [factorALevel2, factorBLevel2]
                    ],
                    [
                        [factorALevel2, factorBLevel1], [factorALevel1, factorBLevel2]
                    ],
                    [
                        [factorALevel1, factorBLevel2], [factorALevel2, factorBLevel1]
                    ],
                    [
                        [factorALevel2, factorBLevel2], [factorALevel1, factorBLevel1]
                    ]
                ]
        """

        within_factor_conditions = [
            factor.get_conditions() for factor in self.within_subject_factors
        ]

        participant_conditions = [[
            list(combination)
            for combination in product(*list(condition_groups))
        ] for condition_groups in product(*within_factor_conditions)]

        return participant_conditions

    def _get_num_conditions_per_participant(self):

        return reduce(lambda prev, cur: prev * cur.get_multiplier(),
                      self.within_subject_factors, 1)

    def _get_min_num_participants(self):

        return reduce(
            lambda prev, cur: prev * cur.get_multiplier(),
            self.between_subject_factors + self.within_subject_factors, 1)


if __name__ == '__main__':

    config = {
        'independentVariables': {
            'phone': {
                'levels': ['iphone', 'huawei', 'samsung'],
                'design': FactorType.between_subject.name,
            },
            'gender': {
                'levels': ['male', 'female'],
                'design': FactorType.between_subject.name,
            },
            'browser': {
                'levels': ['safari', 'chrome', 'IE'],
                'design': FactorType.within_subject.name,
                'order': OrderType.latin_square.name,
            },
            'input': {
                'levels': ['voice', 'touch', 'mouse'],
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

    print(design.get_experimental_design())
