vet = []
i = 0
while i < 100:
    aux = float(input())
    vet.append(aux)
    if vet[i] <= 10:
        print("A[%d] = %.1f"%(i,vet[i]))
    i+=1
