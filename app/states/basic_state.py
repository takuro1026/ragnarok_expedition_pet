import pynecone as pc
from app.services.tactic_service import TacticService


class BasicState(pc.State):
    _service = TacticService()
