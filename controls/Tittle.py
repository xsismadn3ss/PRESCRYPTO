from flet import Text


class Tittle(Text):
    def __init__(self, text: str):
        super().__init__()
        self.value = text
        self.size = 45
