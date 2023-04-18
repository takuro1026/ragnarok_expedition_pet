from dataclasses import dataclass


@dataclass(frozen=True)
class Polly:
    head: str
    body: str
    around: str
