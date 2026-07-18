class BaseRule:
    """
    Base class for all parameter rules.
    """

    def matches(self, parameter_name: str) -> bool:
        raise NotImplementedError

    def generate(self):
        raise NotImplementedError