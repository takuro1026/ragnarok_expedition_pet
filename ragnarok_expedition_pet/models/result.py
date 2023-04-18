from dataclasses import dataclass, field

from ragnarok_expedition_pet.models.polly import Polly


@dataclass
class Result:
    best_polly: Polly
    weight: int
    best_potential_match: field(default_factory=list)
