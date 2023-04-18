from dataclasses import dataclass
from enum import Enum
from typing import List


class Part(Enum):
    HEAD = 0
    BODY = 1
    BACK = 2
    FINAL = 3


@dataclass
class Gene:
    name: str
    part: Part
    children: [str] = None
