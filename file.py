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
            if not key:
                key = list(self.content[0])[0]
            values = []
            for dictionary in self.content:
                values.append(dictionary[key])
            sorteds = radix_sort(values)
            sorted_dict = []
            for value in sorteds:
                i = binary_search(values, value)
                dictionary = self.content[i]
                sorted_dict.append(dictionary)
    def save(self) -> None:
        '''Salva as alterações feitas no conteúdo.'''
        pass

if __name__ == '__main__':
    file = File('admins', 'users')
    print(file.path)
    print(file.content, type(file.content))
    file.sort()
