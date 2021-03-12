temp = int(input("Qual a temperatura?"))

if temp > 100:
    aguaferve = True
    evaporacao = "muito rápida"
else:
    aguaferve = False
    evaporacao = "não"

print(aguaferve, evaporacao)