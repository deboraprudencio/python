# define e testa a função remove_repetidos
# a função recebe uma lista e a devolve sem elementos repetidos e ordenada

def remove_repetidos(list):
    for i in list:
        while (list.count(i) != 1): list.remove(i)
    return sorted(list)

#print(remove_repetidos(list(input())))

def test_1():
    list = [2, 4, 2, 2, 3, 3, 1]
    assert remove_repetidos(list) == [1, 2, 3, 4]

def test_2():
    assert remove_repetidos([1, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
        