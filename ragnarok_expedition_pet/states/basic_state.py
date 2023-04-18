from ragnarok_expedition_pet.ragnarok_expedition_pet import pc
from ragnarok_expedition_pet.services.tactic_service import TacticService


class BasicState(pc.State):
    _service = TacticService()
