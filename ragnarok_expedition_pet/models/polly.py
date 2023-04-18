from dataclasses import dataclass


@dataclass
class Polly:
    head: str
    body: str
    around: str
