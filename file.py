from os import path, makedirs, remove
from json import loads, dumps
from sort import radix_sort
from search import binary_search

class File():
    def __init__(self, name: str, dir: str = None, ext: str = 'json', encoding: str = 'UTF-8', sort_key: str = None) -> None:
        self.name = name
        self.dir = dir
        self.ext = ext
        self.encoding = encoding
        self.path = self.get_path()
        self.content = self.get_content()
        # Definir chave:
        if sort_key:
            self.sort_key = sort_key
        else:
            self.sort_key = list(self.content[0])[0]
        self.key_values = self.get_key_values()
        self.sort()
    def get_path(self) -> str:
        '''Pega o caminho do arquivo.'''
        filename = f'{self.name}.{self.ext}'
        if self.dir:
            return path.join(path.basename(self.dir), path.basename(filename))
        else:
            return path.basename(filename)
    def get_content(self) -> list[dict]:
        '''Pega o conteúdo do arquivo.'''
        try:
            with open(self.path, 'r', encoding = self.encoding) as file:
                content = file.read()
            return loads(content)
        except:
            return []
    def get_key_values(self) -> list[dict]:
        '''Pega uma lista dos valores da chave principal.'''
        values = []
        for dictionary in self.content:
            values.append(dictionary[self.sort_key])
        return values
    def sort(self) -> None:
        '''Ordena conteúdo do arquivo pelo valor da chave passada, se não tiver, é usada a primeira.'''
        if len(self.content) > 0:
            # Ordenar lista:
            sorteds = radix_sort(self.key_values)
            # Coloca os dicionários em ordem a partir da lista ordenada:
            sorted_dicts = []
            for s in range(len(sorteds)):
                for v in range(len(self.key_values)):
                    if sorteds[s] == self.key_values[v]:
                        sorted_dicts.append(self.content[v])
            self.content = sorted_dicts
            self.key_values = sorteds
    def add(self, content: dict) -> None:
        '''Adiciona um novo elemento no arquivo.'''
        pass
    def remove(self, content: dict) -> None:
        '''Remove um elemento do arquivo.'''
        pass
    def save(self) -> None:
        '''Salva as alterações feitas no conteúdo.'''
        pass

if __name__ == '__main__':
    file = File('admins', 'users')
    new_admin = {
        'username' : 'kely',
        'password' : 'asmin'
    }
    file.add(new_admin)
    for c in file.content:
        print(c['username'])
    print(file.key_values)
