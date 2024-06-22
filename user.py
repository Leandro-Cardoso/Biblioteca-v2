class User():
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

class Author(User):
    def __init__(self, username: str, password: str, name: str, date_birth: str, biography: str, research_areas: list) -> None:
        super().__init__(username, password)
        self.name = name
        self.date_birth = date_birth
        self.biography = biography
        self.research_areas = research_areas

class Librarian(User):
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)

class Admin(Librarian):
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
