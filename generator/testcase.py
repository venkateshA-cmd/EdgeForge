from dataclasses import dataclass


@dataclass
class TestCase:
    """
    Represents one generated test case.
    """

    function_name: str

    inputs: list

    reason: str