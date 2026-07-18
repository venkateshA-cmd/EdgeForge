from dataclasses import dataclass, field
from typing import List

from models.function_info import FunctionInfo
from models.class_info import ClassInfo


@dataclass
class AnalysisResult:
    """
    Represents the complete analysis result.
    """

    functions: List[FunctionInfo] = field(default_factory=list)

    classes: List[ClassInfo] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)