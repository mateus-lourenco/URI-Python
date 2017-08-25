vet = []
i = 0

valor = int(input())
while i < 10:    
    vet.append(valor)
    print("N[%d] = %d"%(i,vet[i]))
    valor*=2
    i+=1
