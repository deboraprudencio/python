# define e testa a função concatenar_listas()
    # recebe dois números duas sequências com números inteiros
    # devolve uma sequência ordenada contendo todos os elementos das originais, sem repetição

n = input().split()
m = input().split()

list = n + m

for i in range(len(list)):
    while (list.count(list[i]) != 1): list.remove(list[i])
    list[i] = int(list[i])

print(sorted(list))