# Recebe uma lista de temperaturas e retorna as temperaturas mínima e máxima

def temperaturas_extremas(list):
    max = min = list[0]

    for temp in list:
        if (temp > max): max = temp
        if (temp < min): min = temp
    
    return [max, min]