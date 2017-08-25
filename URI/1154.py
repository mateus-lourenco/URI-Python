parada = True
cont = 0
media = 0

while parada:
    idade = int(input())
    if idade < 0:
        parada=False
    else:
        cont += 1
        media+=idade
print("%.2f"%(media/cont))
    
    
