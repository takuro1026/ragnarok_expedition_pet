import pynecone as pc

from ragnarok_expedition_pet import Gene
from ragnarok_expedition_pet.states.basic_state import BasicState


class FusionState(BasicState):
    items = []

    def list_formula(self, value):
        self.items.clear()
        self._service.generate_formula(value)


