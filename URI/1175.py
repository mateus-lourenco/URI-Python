vet = []
for i in range(20):
    recheio = int(input())
    vet.append(recheio)
aux = 0
j = -1
k = 0
while k < len(vet)*0.5:
    aux = vet[k]
    vet[k] = vet[j]
    vet[j] = aux    
    j-=1
    k+=1
for i in range(20):
    print("N[%d] = %d"%(i,vet[i]))
