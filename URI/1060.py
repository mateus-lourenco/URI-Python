valor = []
i = 0
contador = 0
while (i < 6):
    valor.append(float(input()))
    if(valor[i] > 0.0):
        contador += 1    
    i = i + 1
print(str(int(contador))+" valores positivos")
