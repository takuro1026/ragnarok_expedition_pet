from pcconfig import config
import pynecone as pc

from app.pages.fusion import fusion
from app.pages.index import index
from app.states.basic_state import BasicState


# Add state and page to the app.
app = pc.App(state=BasicState)
app.add_page(index, title="寵物最佳配對")
app.add_page(fusion, title="合成表查詢")
app.compile()

