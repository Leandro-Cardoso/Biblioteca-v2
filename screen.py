from os import name, system

class Screen():
    def __init__(self, title: str, description: str = None, menu: list = ['voltar']) -> None:
        self.title = self.format_title(title)
        self.description = description
        if description:
            self.description = self.format_description(description)
        self.menu = self.format_menu(menu)
    def format(self, string: str) -> str:
        '''Formatação geral das strings.'''
        # Remove espaços:
        strings = string.split(' ')
        for i in range(len(strings) - 1, -1, -1):
            if strings[i] == '':
                del strings[i]
        string = ' '.join(strings)
        return string
    def format_title(self, title: str) -> str:
        '''Formatação do titulo da tela.'''
        title = self.format(title)
        title = title.upper()
        return f'\n> {title}:\n'
    def format_description(self, description: str) -> str:
        '''Formatação da descrição da tela.'''
        description = self.format(description)
        # Primeira letra maiuscula:
        char = description[0].upper()
        description = char + description[1:]
        # Por ponto final:
        if description[-1].isalnum():
            description += '.'
        # TODO -> Colocar maiuscula depois de por pontuação ".", ":", ";", "?", "!":
        return f'\n{description}\n'
    def format_menu(self, menu: list) -> str:
        '''Formatação do menu da tela.'''
        string = '\n'
        for i, option in enumerate(menu):
            string += (
                f'   {i + 1} - ' +
                self.format(option).title() +
                '\n')
        return string
    def clean(self) -> None:
        '''Limpar tela.'''
        print(name)
        if name == 'posix':
            system('clear')
        else:
            system('cls')
    def show(self, menu: bool = True) -> None:
        '''Desenha a tela.'''
        self.clean()
        screen = self.title
        if self.description:
            screen += self.description
        if menu:
            screen += self.menu
        print(screen)
