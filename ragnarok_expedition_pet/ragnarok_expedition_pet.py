"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

from ragnarok_expedition_pet.models.gene import Gene, Part
from ragnarok_expedition_pet.services.tactic_service import TacticService

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class ExampleState(pc.State):
    # The colors to cycle through.
    colors = ["black", "red", "green", "blue", "purple"]

    # The index of the current color.
    index = 0

    _service = TacticService()

    def next_color(self):
        """Cycle to the next color."""
        self.index = (self.index + 1) % len(self.colors)

    @pc.var
    def color(self):
        return self.colors[self.index]


def index():
    return pc.heading(
        "Welcome to Pynecone!",
        on_click=ExampleState.next_color,
        color=ExampleState.color,
        _hover={"cursor": "pointer"},
    )


# Add state and page to the app.
app = pc.App(state=ExampleState)
app.add_page(index)
app.compile()
