import ast

from analyzer.findings import Finding


class RuleEngine:
    """
    Runs analysis rules on parsed code.
    """

    def analyze_function(self, function):

        findings = []

        for statement in function.body:

            if not isinstance(statement, ast.Return):
                continue

            value = statement.value

            if not isinstance(value, ast.BinOp):
                continue

            if not isinstance(value.op, ast.Div):
                continue

            denominator = value.right

            # Safe: constant values like 2, 5, 100
            if isinstance(denominator, ast.Constant):
                continue

            findings.append(
                Finding(
                    title="Possible Division By Zero",
                    description=(
                        "Division uses a variable or expression as the "
                        "denominator. Validate it is not zero."
                    ),
                    severity="HIGH",
                    function_name=function.name,
                )
            )

        return findings