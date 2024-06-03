from flet import TextField
from flet import colors


class TextFieldCustom(TextField):
    def __init__(self, text: str, psswrd: bool = False):
        """Custom text field constructor

        Args:
            text (str): text field description
            psswrd (bool, optional): Mark true to hide sensitive text. Defaults to False.
        """
        super().__init__()
        self.label = text
        self.border_radius = 10
        self.border_color = colors.GREEN_600
        self.focused_border_color = colors.GREEN_300
        self.password = psswrd
