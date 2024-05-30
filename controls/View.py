from flet import Container, colors, Column


class View(Container):
    def __init__(self, controls, *args, **kwargs):
        super().__init__()
        self.content = Column(controls=controls)
        self.padding = 8
