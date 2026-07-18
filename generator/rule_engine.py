from generator.rules.email_rule import EmailRule
from generator.rules.password_rule import PasswordRule
from generator.rules.username_rule import UsernameRule
from generator.rules.numeric_rule import NumericRule


class RuleEngine:

    def __init__(self):

        self.rules = [
            EmailRule(),
            PasswordRule(),
            UsernameRule(),
            NumericRule(),
        ]

    def generate_values(self, parameter_name: str):

        for rule in self.rules:

            if rule.matches(parameter_name):
                return rule.generate()

        return [
            None,
            "",
        ]