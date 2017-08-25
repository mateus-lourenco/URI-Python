t = int(input())
vet = list(range(1000))
i = 0
for j in range(len(vet)):
    print("N[%d] = %d"%(j, vet[i]))
    i+=1
    if i == t:
        i = 0
