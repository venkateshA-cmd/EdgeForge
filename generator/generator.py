from generator.rule_engine import RuleEngine
from generator.testcase import TestCase


class EdgeCaseGenerator:

    def __init__(self):

        self.rule_engine = RuleEngine()

    def generate(self, analysis_result):

        test_cases = []

        for function in analysis_result.functions:

            parameter_sets = []

            for parameter in function.parameters:

                values = self.rule_engine.generate_values(
                    parameter.name
                )

                parameter_sets.append(values)

            if not parameter_sets:
                continue

            max_cases = max(len(values) for values in parameter_sets)

            for index in range(max_cases):

                inputs = []

                for values in parameter_sets:

                    if index < len(values):
                        inputs.append(values[index])
                    else:
                        inputs.append(values[-1])

                test_cases.append(
                    TestCase(
                        function_name=function.name,
                        inputs=inputs,
                        reason="Generated using rule engine",
                    )
                )

        return test_cases