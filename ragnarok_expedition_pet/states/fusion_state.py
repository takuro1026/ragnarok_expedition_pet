import uuid

import pynecone as pc

from ragnarok_expedition_pet.states.basic_state import BasicState


class FusionFormula(pc.Model, table=False):
    id: str = str(uuid.uuid1())
    title: str
    indent: int
    formula: list


class FusionState(BasicState):
    items: list[FusionFormula] = []

    @staticmethod
    def __intersperse(lst, item):
        result = [item] * (len(lst) * 2 - 1)
        result[0::2] = lst
        return result

    def list_formula(self, value):
        self.items.clear()
        result = self._service.generate_formula(value)

        for item in result:
            self.items.append(
                FusionFormula(
                    title=item[0],
                    formula=FusionState.__intersperse(item[1], '+'),
                    indent=item[2]
                )
            )
