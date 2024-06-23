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
        self.sort_key = sort_key
        self.path = self.get_path()
        if path.exists(dir):
            self.content = self.get_content()
            # Definir chave:
            if not sort_key:
                self.sort_key = list(self.content[0])[0]
            self.key_values = self.get_key_values()
            # Ordenar conteúdo:
            self.sort()
        else:
            self.content = []
            self.key_values = []
            # Criar diretório:
            makedirs(dir)
            self.save()
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
            self.sort_key = None
            return []
    def get_key_values(self) -> list[dict]:
        '''Pega uma lista dos valores da chave principal.'''
        values = []
        for dictionary in self.content:
            print(dictionary, self.sort_key)
            values.append(dictionary[self.sort_key])
        return values
    def sort(self) -> None:
        '''Ordena conteúdo do arquivo pelo valor da chave passada, se não tiver, é usada a primeira.'''
        if len(self.content) > 0 and self.sort_key:
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
    def add(self, dictionary: dict) -> None:
        '''Adiciona um novo elemento no arquivo.'''
        # Definir chave:
        if not self.sort_key:
            self.sort_key = list(dictionary)[0]
        # Buscar:
        i = binary_search(self.key_values, dictionary[self.sort_key])
        if i == -1:
            # Adicionar:
            self.content.append(dictionary)
            self.key_values.append(dictionary[self.sort_key])
            self.sort()
        else:
            # Sobrescrever:
            self.content[i] = dictionary
    def remove(self, dictionary: dict) -> None:
        '''Remove um elemento do arquivo.'''
        if self.sort_key:
            i = binary_search(self.key_values, dictionary[self.sort_key])
            if i != -1:
                del self.content[i]
                del self.key_values[i]
        # Definir chave:
        if len(self.content) == 0:
            self.sort_key = None
    def save(self) -> None:
        '''Salva as alterações feitas no conteúdo.'''
        with open(self.path, 'w', encoding = self.encoding) as file:
            file.write(dumps(self.content))

if __name__ == '__main__':
    file = File('admins', 'users')
    user = {
        'username' : 'xuxa',
        'password' : 'admin'
    }
    file.remove(user)
    for c in file.content:
        print(c['username'])
    print(file.key_values)
    file.save()

    doc = File('documents', 'documents')
    document = {
        'title' : 'harry potter',
        'author' : 'j k rowling'
    }
    doc.add(document)
    doc.save()
