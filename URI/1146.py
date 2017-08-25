parada = True

while parada:
    i = 1
    saida = ""
    x = int(input())
    if x == 0:
        parada = False
        
    while i <= x:
        saida+=str(i) +" "
        i+=1
    if saida != "":
        print(saida.strip())

