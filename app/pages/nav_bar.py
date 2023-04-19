import pynecone as pc


def navbar():
    return pc.box(
        pc.hstack(
            pc.link("寵物最佳配對", href="/", font_weight="medium"),
            pc.link("合成表查詢", href="/fusion", font_weight="medium"),
            # pc.hstack(
            #     pc.cond(
            #         State.user,
            #         pc.hstack(
            #             pc.link(
            #                 "Log out",
            #                 color="blue.600",
            #                 on_click=LoginState.log_out,
            #             ),
            #             pc.avatar(name=State.user.email, size="md"),
            #             spacing="1rem",
            #         ),
            #         pc.box(),
            #     )
            # ),
            justify_content="space-around",
        ),
        width="100%",
        padding="1rem",
        margin_bottom="2rem",
        border_bottom="1px solid black",
    )