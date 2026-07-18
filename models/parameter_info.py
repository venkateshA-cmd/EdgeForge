from dataclasses import dataclass
from typing import Any

@dataclass
class ParameterInfo:
    """
    Represents one parameter of a python function
    
    """
    name:str
    annotation:str | None
    default:Any = None
    