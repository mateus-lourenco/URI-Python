qtd = int(input())
i = 0
lista = []
cont1 = 0
cont2 = 0

while i < qtd:
    lista.append(int(input()))
    if(lista[i] >= 10 and lista[i] <= 20):
        cont1 += 1
    else:
        cont2 += 1
    i += 1
        
print("%d in"%cont1)
print("%d out"%cont2)
        
