from dataclasses import dataclass


@dataclass
class Finding:
    """
    Represents one issue found during analysis.
    """

    title: str

    description: str

    severity: str

    function_name: str