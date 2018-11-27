import enum

from factors import Factor, FactorType


def parse_config(config, warning=False):

    independent_variables = config.get('independentVariables', None)
    assert independent_variables, "Independent variables field can not be None"

    parsed_config = {}

    # parse independent variables
    for variable_name in independent_variables:
        try:
            factor_type = independent_variables[variable_name]['design']
            factors_list = parsed_config.get(factor_type, [])

            if factor_type == FactorType.between_subject.name:
                factors_list += [
                    Factor(
                        name=variable_name,
                        levels=independent_variables[variable_name]['levels'],
                        design=FactorType.between_subject.name)
                ]
            elif factor_type == FactorType.within_subject.name:
                factors_list += [
                    Factor(
                        name=variable_name,
                        levels=independent_variables[variable_name]['levels'],
                        design=FactorType.within_subject.name,
                        order=independent_variables[variable_name]['order'])
                ]

            parsed_config[factor_type] = factors_list

        except Exception as e:
            print(e)

    return parsed_config


if __name__ == '__main__':
    pass
