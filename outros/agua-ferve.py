#recebe uma temperatura e retorna se a água ferve e evapora ou não

temp = int(input("Qual a temperatura?"))

if temp > 100:
    aguaferve = True
    evaporacao = "muito rápida"
else:
    aguaferve = False
    evaporacao = "não"

print(aguaferve, evaporacao)