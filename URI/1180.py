vet = []
i = 0
tam = int(input())
while i < tam:
    a = input().split(" ")
    a = int(a)
    vet.append(a)
    i+=1
print("Menor valor: %d"%min(vet))
print("Posicao: %d"%vet.index(min(vet)))
