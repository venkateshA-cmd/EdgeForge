from analyzer.rules import RuleEngine


class Analyzer:

    def __init__(self):

        self.rule_engine = RuleEngine()

    def analyze(self, analysis_result):

        findings = []

        for function in analysis_result.functions:

            findings.extend(
                self.rule_engine.analyze_function(function)
            )

        return findings