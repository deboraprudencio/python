# Recebe um número inteiro n e uma sequência com n números reais
# Devovle a maior soma de um segmento da sequência (com pelo menos um elemento)
# Um segmento é uma subsequência de números consecutivos.

def add_list(list):
    soma = 0

    for i in list: soma += i

    return soma

def max_soma(list):
    max_soma = list[0]

    for i in range(len(list)):
        j = i + 1
        while (j <= len(list)):
            if (add_list(list[i:j]) > max_soma): max_soma = add_list(list[i:j])
            j += 1
    
    return max_soma

print(max_soma([-5, -10, -8, -23, -100, -30, -60, -1]))

# def read_list():
#     n = int(input())
#     list = []

#     while (n > 0):
#         list.append(int(input()))
#         n -= 1
    
#     return list

# print(max_soma(read_list()))


# Para n == 12 e a sequência [5   -2   -2   -7   3   14  10  -3   9   -6   4   1]
# A soma do segmento de soma máxima é 3+14+10-3+9 = 33.
