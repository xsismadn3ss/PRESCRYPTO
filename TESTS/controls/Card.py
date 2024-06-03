from flet import Container, Column, colors, Row


class Card(Row):
    def __init__(
        self,
        controls,
        bgcolor=None,
        width=None,
        height=None,
        on_click=None,
        on_long_press=None,
        data: str = None,
    ):
        super().__init__()
        self.controls = [
            Container(
                content=Column(controls=controls),
                bgcolor=bgcolor,
                border_radius=10,
                padding=20,
                expand=1,
                on_click=on_click,
                on_long_press=on_long_press,
                data=data,
            )
        ]
