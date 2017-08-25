numero = int(input())
i = 1
while i <= 6:
    if numero % 2 != 0:
        print(numero)
        numero+=1
    else:
        numero+=1
        i-=1
    i+=1
