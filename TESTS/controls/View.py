from flet import Container, colors, Column, ListView


class View(ListView):
    def __init__(self, controls, aligment=None, height=None, color=None):
        """Custom view constructor

        Args:
            controls (flet control): add a list of controls to fill your view
            aligment (_type_, optional): aligment contraint. Defaults to None.
            height (_type_, optional): hegih constraint. Defaults to None.
            color (_type_, optional): background color. Defaults to None.
        """
        super().__init__()
        self.padding = 10
        self.height = height
        self.controls = [
            Container(
                content=Column(controls=controls, alignment=aligment),
                height=height,
                padding=10,
                border_radius=10,
                bgcolor=color,
            ),
        ]
        self.expand = 1
        self.spacing = 10
        self.padding = 8
        self.auto_scroll = True
