valor = []
i = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

while (i < 5):
    valor.append(float(input()))
    if(valor[i] % 2 == 0.0):
        contador1 += 1
    if(valor[i] % 2 != 0.0):
        contador2 += 1
    if(valor[i] > 0.0):
        contador3 += 1
    if(valor[i] < 0.0):
        contador4 += 1        
    i = i + 1
    
print(str(int(contador1))+" valor(es) par(es)")
print(str(int(contador2))+" valor(es) impar(es)")
print(str(int(contador3))+" valor(es) positivo(s)")
print(str(int(contador4))+" valor(es) negativo(s)")
