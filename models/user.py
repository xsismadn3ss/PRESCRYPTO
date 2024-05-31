class User:
    def __init__(
        self,
        name: str = None,
        lastname: str = None,
        id: str = None,
        prescriptions=None,
    ) -> None:
        self.name = name
        self.lastname = lastname
        self.id = id
        self.prescriptions = prescriptions
