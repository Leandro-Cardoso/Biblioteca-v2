def binary_search(arr:list, key:str) -> int:
    '''Algoritmo de busca binária.'''
    s = 0
    e = len(arr) - 1
    while e > 0:
        m = (s + e) // 2
        if arr[m] == key:
            return m
        elif arr[m] < key:
            s = m + 1
        else:
            e = m - 1
    return -1
