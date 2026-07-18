from dataclasses import dataclass, field
from typing import Any

from models.parameter_info import ParameterInfo


@dataclass
class FunctionInfo:
    """
    Represents one Python function.
    """

    name: str

    parameters: list[ParameterInfo] = field(default_factory=list)

    return_annotation: str | None = None

    line_number: int = 0

    docstring: str | None = None

    body: list[Any] = field(default_factory=list)