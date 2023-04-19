import uuid

import pynecone as pc

from app.models.polly import Polly
from app.services import BASIC_POLLY
from app.states.basic_state import BasicState


class MatchedFormula(pc.Model, table=False):
    id: str = str(uuid.uuid1())
    matched_polly: str
    matched_head: str
    matched_body: str
    matched_around: str

    result_head: str
    result_body: str
    result_around: str

    matched_parts: str

    best_combination: list


class IndexState(BasicState):
    head: str
    body: str
    around: str

    matched_result: list[MatchedFormula]

    @pc.var
    def searchable(self) -> bool:
        return len(self.head) != 4 or len(self.body) != 4 or len(self.around) != 4

    def search(self):
        self.matched_result.clear()

        current_polly = Polly("current_polly", self.head, self.body, self.around)

        for polly in BASIC_POLLY:
            result = self._service.find_combination(
                current_polly,
                polly
            )

            if result.best_potential_match is not None:
                max_parts_matched = "(有3個部位符合)" if result.weight >= 1000 else "(有2個部位符合)"

                self.matched_result.append(
                    MatchedFormula(
                        matched_polly=polly.num,
                        matched_head=polly.head,
                        matched_body=polly.body,
                        matched_around=polly.around,
                        result_head=result.best_polly.head,
                        result_body=result.best_polly.body,
                        result_around=result.best_polly.around,
                        best_combination=result.best_potential_match,
                        matched_parts=max_parts_matched
                    )
                )
