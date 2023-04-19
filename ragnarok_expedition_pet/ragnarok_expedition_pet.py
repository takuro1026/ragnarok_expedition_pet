from pcconfig import config
import pynecone as pc

from ragnarok_expedition_pet.pages.fusion import fusion
from ragnarok_expedition_pet.pages.index import index
from ragnarok_expedition_pet.states.basic_state import BasicState


# Add state and page to the app.
app = pc.App(state=BasicState)
app.add_page(index, title="寵物最佳配對")
app.add_page(fusion, title="合成表查詢")
app.compile()

