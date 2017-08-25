vet = []
i = 0
while i < 10:
    valor = int(input())
    vet.append(valor)

    if vet[i] <= 0:
        vet[i] = 1
    print("X[%d] = %d" % (i, vet[i]))
    i += 1