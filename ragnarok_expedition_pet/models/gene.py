from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Part(Enum):
    HEAD = 0
    BODY = 1
    AROUND = 2
    FINAL = 3


class Level(Enum):
    BASIC = 0
    ADVANCED = 1
    FINAL = 2


@dataclass
class Gene:
    name: str
    part: Part
    children: [str] = field(default_factory=list)
    parent: [str] = field(default_factory=list)

    def get_level(self):
        if len(self.parent) == 0:
            return Level.FINAL
        elif len(self.children) == 0:
            return Level.BASIC
        else:
            return Level.ADVANCED
