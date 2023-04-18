import pynecone as pc
from ragnarok_expedition_pet.services.tactic_service import TacticService


class BasicState(pc.State):
    _service = TacticService()
