from os import path, makedirs, remove
from json import loads, dumps
from sort import radix_sort
from search import binary_search

class File():
    def __init__(self, name: str, dir: str = None, ext: str = 'json', encoding: str = 'UTF-8') -> None:
        self.name = name
        self.dir = dir
        self.ext = ext
        self.encoding = encoding
        self.path = self.get_path()
        self.content = self.get_content()
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
    def sort(self, key: str = None) -> None:
        '''Ordena conteúdo do arquivo pelo valor da chave passada, se não tiver, é usada a primeira.'''
        if len(self.content) > 0:
            # Definir chave:
            if not key:
                key = list(self.content[0])[0]
            # Criar uma lista com os valores das chaves:
            values = []
            for dictionary in self.content:
                values.append(dictionary[key])
            # Ordenar lista:
            sorteds = radix_sort(values)
            # Coloca os dicionários em ordem a partir da lista ordenada:
            sorted_dicts = []
            for s in range(len(sorteds)):
                for v in range(len(values)):
                    if sorteds[s] == values[v]:
                        sorted_dicts.append(self.content[v])
            self.content = sorted_dicts
    def save(self) -> None:
        '''Salva as alterações feitas no conteúdo.'''
        pass

if __name__ == '__main__':
    file = File('admins', 'users')
    for c in file.content:
        print(c['username'])
