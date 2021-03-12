#recebe 3 números e retorna se eles estrão em ordem crescente ou não

n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 < n2) and (n2 < n3): print("crescente")
else: print("não está em ordem crescente")
