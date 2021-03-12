n = int(input())
dif = True

while (len(str(n)) >= 2) and dif:
    lastDig = n % 10
    prevDig = (n // 10) % 10

    n = n // 10

    if (lastDig == prevDig):
        dif = False
        print("sim")

if dif:
    print ("não")
