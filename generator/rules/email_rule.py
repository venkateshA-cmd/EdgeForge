from generator.rules.base_rule import BaseRule


class EmailRule(BaseRule):

    def matches(self, parameter_name: str) -> bool:
        return "email" in parameter_name.lower()

    def generate(self):
        return [
            "user@example.com",
            "",
            "invalid-email",
        ]