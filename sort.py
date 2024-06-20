def bucket_sorter(strings:list, c:int) -> list:
    # Criar buckets:
    n_buckets = 128
    buckets = [[] for i in range(n_buckets)]
    # Pegar o caracter na mesma posição de cada string e colocar no bucket correspondente:
    for string in strings:
        b = ord(string[c])
        buckets[b].append(string)
    # Concatenar buckets em uma lista:
    result = []
    for bucket in buckets:
        result += bucket
    return result

def radix_sort(strings:list) -> list:
    # Pegar tamanho da maior string:
    longest = max(len(string) for string in strings)
    # Justificar strings para esquerda e completando com o "separator" até o tamanho da maior string:
    separator = '#'
    strings = [string.ljust(longest, separator) for string in strings]
    # Percorer os caracteres um de cada vez no sentido contrario e alternar entre eles:
    for c in range(longest - 1, -1, -1):
        strings = bucket_sorter(strings, c)
    # Remover espaços:
    strings = [string.strip(separator) for string in strings]
    return strings
