class Menu():
    def __init__(self, options: list, inputname: str = 'OPÇÃO') -> None:
        self.options = options
        self.inputname = inputname
    def get_choice(self) -> int:
        while True:
            choice = input(f' {self.inputname}: ')
            if choice.isnumeric():
                choice = int(choice)
                if 0 < choice < len(self.options) + 1:
                    return choice
                else:
                    print(f'\n [ERRO] {choice} não é uma opção valida.\n')
            else:
                print(f'\n [ERRO] {choice} precisa ser um número inteiro.\n')
