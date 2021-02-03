class User:
    def __init__(
        self,
        id: str,
        email: str,
        password: str
    ):
        self._id = id
        self._email = email
        self._password = password