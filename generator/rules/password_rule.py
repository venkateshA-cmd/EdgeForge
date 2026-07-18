from generator.rules.base_rule import BaseRule


class PasswordRule(BaseRule):

    def matches(self, parameter_name: str) -> bool:
        return "password" in parameter_name.lower()

    def generate(self):
        return [
            "password123",
            "",
            "wrong_password",
        ]