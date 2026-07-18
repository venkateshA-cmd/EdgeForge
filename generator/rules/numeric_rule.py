from generator.rules.base_rule import BaseRule


class NumericRule(BaseRule):

    NUMERIC_NAMES = {
        "a",
        "b",
        "x",
        "y",
        "count",
        "age",
        "price",
        "amount",
        "total",
        "number",
        "value",
    }

    def matches(self, parameter_name: str) -> bool:
        return parameter_name.lower() in self.NUMERIC_NAMES

    def generate(self):
        return [
            1,
            0,
            -1,
        ]