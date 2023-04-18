from ragnarok_expedition_pet.ragnarok_expedition_pet import pc
from ragnarok_expedition_pet.states.index_state import IndexState


def index():
    return pc.heading(
        "魔物遠征簡易寵物合成查詢系統",
        on_click=IndexState.next_color,
        color=IndexState.color,
        _hover={"cursor": "pointer"},
    )
