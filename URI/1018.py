valor = float(input())
notas = [100, 50, 20, 10, 5, 2, 1]

i = 0
resultado = 0

print(str(int(valor)))

while i < 7 :
    
    resultado = valor / notas[i]
    print( str(int(resultado))+" nota(s) de R$ "+str(int(notas[i]))+",00")
    resultado = valor % notas[i]
    valor = resultado
    i = i + 1
