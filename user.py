class User():
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

class Librarian(User):
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)

class Admin(Librarian):
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
