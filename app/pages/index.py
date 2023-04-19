import pynecone as pc

from app.pages.nav_bar import navbar
from app.services import ALL_HEAD_GENES, ALL_BODY_GENES, ALL_AROUND_GENES
from app.states.index_state import IndexState, MatchedFormula


def render_item(item: MatchedFormula):
    """Render an item in the todo list."""
    return pc.hstack(
        pc.text(item.matched_polly, font_size="1.25em"),
        pc.badge(item.matched_head, variant="solid", color_scheme="green", font_size="1.25em"),
        pc.text(" + ", font_size="1.25em"),
        pc.badge(item.matched_body, variant="solid", color_scheme="blue", font_size="1.25em"),
        pc.text(" + ", font_size="1.25em"),
        pc.badge(item.matched_around, variant="solid", color_scheme="orange", font_size="1.25em"),
        pc.text(" => ", font_size="1.25em"),
        pc.badge(item.result_head, variant="solid", color_scheme="green", font_size="1.25em"),
        pc.text(" + ", font_size="1.25em"),
        pc.badge(item.result_body, variant="solid", color_scheme="blue", font_size="1.25em"),
        pc.text(" + ", font_size="1.25em"),
        pc.badge(item.result_around, variant="solid", color_scheme="orange", font_size="1.25em"),
        pc.text(" = ", font_size="1.25em"),
        pc.foreach(
            item.best_combination,
            render_formula
        ),
        pc.text(item.matched_parts, font_size="1.25em")
    )


def render_formula(item):
    return pc.hstack(
        pc.badge(item, font_size="1.25em"),
    )


def index():
    return pc.vstack(
        navbar(),
        index_content()
    )


def index_content():
    head_gene_names = [gene.name for gene in ALL_HEAD_GENES]
    body_gene_names = [gene.name for gene in ALL_BODY_GENES]
    around_gene_names = [gene.name for gene in ALL_AROUND_GENES]

    return pc.vstack(
        pc.heading("寵物最佳配對"),
        pc.box(padding=3),
        pc.hstack(
            pc.select(
                head_gene_names,
                placeholder="請選擇當前寵物的頭部基因",
                on_change=IndexState.set_head
            ),
            pc.select(
                body_gene_names,
                placeholder="請選擇當前寵物的身體基因",
                on_change=IndexState.set_body
            ),
            pc.select(
                around_gene_names,
                placeholder="請選擇當前寵物的配件基因",
                on_change=IndexState.set_around
            ),
            pc.button(
                "Search", bg="lightblue", color="black", size="lg", is_disabled=IndexState.searchable,
                on_click=IndexState.search
            )
        ),
        pc.box(padding=3),
        pc.foreach(
            IndexState.matched_result,
            render_item
        )
    )
