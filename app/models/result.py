from dataclasses import dataclass, field

from app.models.polly import Polly


@dataclass(frozen=True)
class Result:
    best_polly: Polly
    weight: int
    best_potential_match: field(default_factory=list)
