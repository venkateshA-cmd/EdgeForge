from dataclasses import dataclass, field
from typing import List

from models.function_info import FunctionInfo


@dataclass
class ClassInfo:
    """
    Represents one Python class.
    """

    name: str

    methods: List[FunctionInfo] = field(default_factory=list)

    bases: List[str] = field(default_factory=list)

    line_number: int = 0

    docstring: str | None = None