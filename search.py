def binary_search(arr:list, key:str, approximate: bool = False) -> int:
    '''Algoritmo de busca binária.'''
    s = 0
    e = len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        print(m)
        if arr[m] == key:
            return m
        elif arr[m] < key:
            s = m + 1
        else:
            e = m - 1
    if approximate:
        return m
    else:
        return -1
