from dataclasses import dataclass


@dataclass(frozen=True)
class Polly:
    num: str
    head: str
    body: str
    around: str
