from generator.rules.base_rule import BaseRule


class UsernameRule(BaseRule):

    def matches(self, parameter_name: str) -> bool:
        return "user" in parameter_name.lower()

    def generate(self):
        return [
            "admin",
            "",
            "wrong_user",
        ]