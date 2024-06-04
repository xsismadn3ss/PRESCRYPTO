from turtle import color
import flet as ft
from flet import (
    ElevatedButton,
    colors,
    Container,
    Column,
    Row,
    TextField,
    Text,
    ListView,
    NavigationBar,
)


class CustomButton(ElevatedButton):
    def __init__(self, text: str, on_click=None, data=None):
        """Add text to your button

        Args:
            text (str): descriptive text
        """
        super().__init__()
        self.text = text
        self.bgcolor = colors.GREEN_900
        self.color = colors.WHITE
        self.on_click = on_click
        self.data = data


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


class TextFieldCustom(TextField):
    def __init__(
        self,
        text: str,
        psswrd: bool = False,
        width: int = None,
        icon=None,
        data=None,
        input_filter=None,
        reveal: bool = False,
        read_only: bool = False,
        text_align: str = None,
        value: str = None,
    ):
        """Custom text field constructor

        Args:
            text (str): text field description
            psswrd (bool, optional): Mark true to hide sensitive text. Defaults to False.
        """
        super().__init__()
        self.value = value
        self.label = text
        self.border_radius = 10
        self.border_color = colors.GREEN_600
        self.focused_border_color = colors.GREEN_300
        self.password = psswrd
        self.width = width
        self.icon = icon
        self.data = data
        self.can_reveal_password = reveal
        self.input_filter = input_filter
        # self.color = colors.LIGHT_GREEN_800
        self.read_only = read_only
        self.text_align = text_align


class Tittle(Text):
    def __init__(self, text: str):
        """Custom Title constructor.

        Flet control designed to be a heading

        Args:
            text (str): _description_
        """
        super().__init__()
        self.value = text
        self.size = 45


class View_normal(ListView):
    def __init__(self, controls, alignment=None, height=None, color=None):
        """Custom view constructor

        Args:
            controls (flet control): add a list of controls to fill your view
            aligment (_type_, optional): aligment contraint. Defaults to None.
            height (_type_, optional): hegih constraint. Defaults to None.
            color (_type_, optional): background color. Defaults to None.
        """
        super().__init__()
        self.controls = [
            Container(
                content=Column(controls=controls, alignment=alignment),
                height=height,
                padding=10,
                border_radius=10,
                bgcolor=color,
            ),
        ]
        self.expand = 1
        self.spacing = 10
        self.padding = 8


class View_centered(View_normal):
    def __init__(self, controls, alignment=None, height=None, color=None):
        super().__init__(controls, alignment, height, color)
        self.controls = [
            Container(
                content=Row(
                    controls=[Column(controls=controls, alignment=alignment)],
                    alignment="center",
                ),
                height=height,
                padding=10,
                border_radius=10,
                bgcolor=color,
            ),
        ]
        self.expand = 1
        self.spacing = 10
        self.padding = 8
