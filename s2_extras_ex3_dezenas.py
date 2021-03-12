#recebe um número inteiro e diz qual é seu dígito das dezenas

num = int(input("Digite um número inteiro: "))

r100 = num % 100
r10 = num % 10

dez = int((r100 - r10) / 10)

print("O dígito das dezenas é", dez)
