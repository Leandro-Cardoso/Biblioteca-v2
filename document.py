class Document():
    def __init__(self, title: str, author: str, date: str, theme: str, historical_context: str, description: str, location: str) -> None:
        self.title = title
        self.author = author
        self.date = date
        self.theme = theme
        self.historical_context = historical_context
        self.description = description
        self.location = location

if __name__ == '__main__':
    pass
