# recebe n números maiores que 0 e retorna o seu máximo divisor comum

n = int(input("Quantos números terá sua sequência? "))
n_old = mdc = 1
i = j = 0

while (i < n):
    n_new = int(input("Digite um número inteiro maior que 0: "))
    if (n_new < n_old): j = n_new # iguala j ao menor dos números para evitar teste desnecessários
    
    while (j > 0): # confere do maior para o menor divisor
        if (n_new % j == 0) and (n_old % j == 0) and ((i == 1) or (mdc % j == 0)): 
        # se ambos os números e, caso não seja o primeiro teste, também o mdc são divisíveis por j...
                mdc = j # ...atualiza o máximo divisor comum para j
                j = 0 # encerra a comparação
        j -= 1

    j = n_old = n_new # atualiza os valores para a próxima comparação
    i += 1

if (n == 1) and (n_new != 0): mdc = n_new
print("Máximo divisor comum:", mdc)


# Casos de teste:
# 4: 5, 5, 5, 5 == 5
# 3: 10, 50, 45 == 5
# 3: 59, 6, 7 == 1 --> nenhuma das comparações encontra um divisor comum maior que 1
# 3: 59, 6, 12 == 1 --> segunda comparação encontra um divisor maior que é divisível pelo anterior (deve manter o menor)
# 3: 12, 60, 3 == 3 --> segunda comparação encontra um divisor menor (deve atualizar para o menor)
# 3: 3, 12, 60 == 3 --> segunda comparação encontra um divisor maior que é divisível pelo anterior (deve manter o menor)
# 3: 144, 120, 60 == 12 --> segunda comparação encontra um divisor maior que não é divisível pelo anterior (deve manter o menor)
# 5: 5, 5, 8, 5, 5 == 1 --> máximo divisor diminui no meio da série de comparações e aumenta de novo (deve manter o menor)
# 4: 16, 24, 60, 100 == 4
# 5: 16, 24, 2, 60, 100 == 2 --> máximo divisor diminui no meio da série de comparações e aumenta de novo (deve manter o menor)
# 4: 2, 4, 8, 16 == 2 --> comparações vão encontrando divisores cada vez maiores (deve manter o menor)
# 4: 16, 8, 4, 2 == 2 --> comparações vão encontrando divisores cada vez menores (deve atualizar para o menor)
# 0: == 1 --> sequência com 0 números (mdc é 1)
# 1: 7 == 7--> sequência de apenas um número (mdc é o número)