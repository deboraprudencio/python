n = int(input())
num_harmonico1 = num_harmonico2 = 0

for i in range(n):
    num_harmonico1 += n / (i + 1)
    num_harmonico2 += n / (n - i)
    print("termos:", num_harmonico1  n / (i + 1), "|", n / (n - i))

print("-----------------------------------------------------------------")
print("resultado:", num_harmonico1, "|", num_harmonico2)

''' O segundo método (direta para esquerda) é mais estável porque, conforme a soma total aumenta, 
    os termos também aumentam, ou seja, a diferença de magnitude entre os números somados é decrescente
'''
''' O primeiro método (esquerda para direita) é instável porque conforme a soma total aumenta,
    os termos diminuem, ou seja, a diferença de magnitude entre os números somados é crescente
'''