from flet import Text


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
