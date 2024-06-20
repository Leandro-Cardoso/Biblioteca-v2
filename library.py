class Library():
    def __init__(self, name: str) -> None:
        self.name = name
        self.admins = self.get_admins()
        self.librarians = self.get_librarians()
        self.books = self.get_books()
    def get_admins(self) -> list:
        '''Retorna todos os admins da biblioteca.'''
        pass
    def get_librarians(self) -> list:
        '''Retorna todos os bibliotecários.'''
        pass
    def get_books(self) -> list:
        '''Retorna todos os livros registrados.'''
        pass
