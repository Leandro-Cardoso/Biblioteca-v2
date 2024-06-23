class Screen():
    def __init__(self, title: str, description: str = None, menu: list = None) -> None:
        self.title = title
        self.description = description
        self.menu = menu
    def draw_title(self) -> None:
        '''Desenha o titulo da tela.'''
    def draw_description(self) -> None:
        '''Desenha a descrição da tela.'''
    def draw_menu(self) -> None:
        '''Desenha o menu da tela.'''
    def draw(self) -> None:
        '''Desenha a tela.'''
