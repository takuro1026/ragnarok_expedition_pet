import pynecone as pc
from ragnarok_expedition_pet.services.tactic_service import TacticService
from ragnarok_expedition_pet.states.basic_state import BasicState


class IndexState(BasicState):
    # The colors to cycle through.
    colors = ["black", "red", "green", "blue", "purple"]

    # The index of the current color.
    index = 0

    def next_color(self):
        """Cycle to the next color."""
        self.index = (self.index + 1) % len(self.colors)

    @pc.var
    def color(self):
        # result = self._service.find_combination(
        #     Polly("幸運葉草", "針織圍巾", "雞毛撢子"),
        #     Polly("蒸蒸日上", "青綠樹枝", "雲霧繚繞")
        # )
        # print(result)
        return self.colors[self.index]