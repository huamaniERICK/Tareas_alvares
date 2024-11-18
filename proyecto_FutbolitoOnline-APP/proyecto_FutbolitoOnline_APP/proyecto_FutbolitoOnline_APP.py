
import reflex as rx

from .componentes.inicio_sesion import seccion
def index()->rx.Component:
    return rx.box(
        seccion(),
    )

app = rx.App()
app.add_page(index)

    





# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
            
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="9",
#             justify="center",
#             min_height="50vh",
#         ),
#         rx.logo(),
#     )


# app = rx.App()
# app.add_page(blur_example)
