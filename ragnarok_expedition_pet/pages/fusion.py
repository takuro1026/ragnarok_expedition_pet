import pynecone as pc

from ragnarok_expedition_pet.pages.nav_bar import navbar
from ragnarok_expedition_pet.services import ALL_ADVANCED_GENES
from ragnarok_expedition_pet.states.fusion_state import FusionState
from ragnarok_expedition_pet.states.index_state import IndexState


def fusion():
    return pc.vstack(
        navbar(),
        fusion_content()
    )


def fusion_content():
    gene_names = [gene.name for gene in ALL_ADVANCED_GENES]
    return pc.vstack(
        pc.heading("合成表查詢"),
        pc.box(padding=3),
        pc.select(
            gene_names,
            placeholder="請選擇想要查詢的基因",
            on_change=FusionState.list_formula
        ),
    )
