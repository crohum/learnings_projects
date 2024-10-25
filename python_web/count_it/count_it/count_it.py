import reflex as rx


# BACKEND code:
class State(rx.State):
    count: int = 0

    def increment(self, amount: int):
        self.count += amount

    def decrement(self, amount: int):
        self.count -= amount


# FRONTEND code:
def index():
    return rx.hstack(
        rx.button(
            "Decrement by 1",
            color_scheme="ruby",
            on_click=lambda: State.decrement(1),
        ),
        rx.button(
            "Decrement by 5",
            color_scheme="ruby",
            on_click=lambda: State.decrement(5),
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment by 1",
            color_scheme="grass",
            on_click=lambda: State.increment(1),
        ),
        rx.button(
            "Increment by 5",
            color_scheme="grass",
            on_click=lambda: State.increment(5),
        ),
        spacing="4",
    )


app = rx.App()
app.add_page(index)
