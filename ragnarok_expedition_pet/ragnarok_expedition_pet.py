"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import pynecone as pc

from ragnarok_expedition_pet.pages.fusion import fusion
from ragnarok_expedition_pet.pages.index import index
from ragnarok_expedition_pet.states.basic_state import BasicState


def custom():
    return pc.text("Custom Route")


# Add state and page to the app.
app = pc.App(state=BasicState)
app.add_page(index)
app.add_page(fusion)
app.add_page(custom, route="/custom-route")
app.compile()
