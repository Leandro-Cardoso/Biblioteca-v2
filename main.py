from library import Library
from file import File
from screen import Screen
from menu import Menu

def create_account() -> None:
    while True:
        screen = Screen(
            'criação de conta',
            'digite um nome de usuário e senha')
        screen.show()
        username = input('USUÁRIO: ')
        if username == '1':
            break

def login() -> None:
    while True:
        screen = Screen(
            'login',
            'digite um nome de usuário e senha')
        screen.show()
        username = input('USUÁRIO: ')
        if username == '1':
            break

def main() -> None:
    while True:
        options = [
            'sair',
            'criar conta',
            'logar'
        ]
        screen = Screen(
            'biblioteca de história',
            'faça o login e tenha acesso a nosso acervo',
            options)
        menu = Menu(options)
        screen.show()
        choice = menu.get_choice()
        if choice == 1:
            screen = Screen(
                'biblioteca de história',
                'volte sempre!!!')
            screen.show(menu = False)
            break
        elif choice == 2:
            create_account()
        elif choice == 3:
            login()

main()
