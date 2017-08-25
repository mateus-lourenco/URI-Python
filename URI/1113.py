parada = True
while parada:
    x, y = map(int, input().split())
    if x < y:
        print("Crescente")
    elif x > y:
        print("Decrescente")
    else:
        parada = False
