#recebe um número de segundos e converte em dias, horas, minutos e segundos

s0 = input("Por favor, entre com o número de segundos que deseja converter:")

s1 = int(s0)
dias = s1 // 86400
s2 = s1 % 86400
horas = s2 // 3600
s3 = s2 % 3600
minutos = s3 // 60
segundos = s3 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")
