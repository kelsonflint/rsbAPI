class User:
    def __init__(
        self,
        id: str,
        email: str,
        password: str,
        firstName: str,
        lastName: str
    ):
        self.id = id
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName