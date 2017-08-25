parada = True
cont = 0
aux = 0
while parada:
    a = float(input())
    if a < 0 or a >10:
        print ("nota invalida")
        
    elif cont == 0:
        aux = a
        cont =1
    else:
        print("media = %.2f"%((a+aux) / 2))
        parada=False
            
