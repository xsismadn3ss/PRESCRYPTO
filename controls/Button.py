from flet import ElevatedButton, colors


class CustomButton(ElevatedButton):
    def __init__(self, text: str):
        """Add text to your button

        Args:
            text (str): descriptive text
        """
        super().__init__()
        self.text = text
        self.bgcolor = colors.GREEN_900
        self.color = colors.WHITE
