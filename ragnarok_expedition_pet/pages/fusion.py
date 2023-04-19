import pynecone as pc

from ragnarok_expedition_pet.pages.nav_bar import navbar
from ragnarok_expedition_pet.services import ALL_ADVANCED_GENES
from ragnarok_expedition_pet.states.fusion_state import FusionState, FusionFormula


def fusion():
    return pc.vstack(
        navbar(),
        fusion_content()
    )


def render_item(item: FusionFormula):
    """Render an item in the todo list."""
    return pc.hstack(
        pc.text(item.title, font_size="1.25em"),
        pc.text(" = ", font_size="1.25em"),
        pc.foreach(
            item.formula,
            render_formula
        )
    )


def render_formula(item):
    return pc.text(item, font_size="1.25em")


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
        pc.box(padding=3),
        pc.foreach(
            FusionState.items,
            render_item
        )
    )
