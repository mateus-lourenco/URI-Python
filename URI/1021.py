valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

i = 0
j = 0

resultado = 0


print("NOTAS:")
while i < 6 :    
     resultado = valor / notas[i]
     print( str(int(resultado))+" nota(s) de R$ %.2f"%notas[i])
     resultado = valor % notas[i]
     valor = resultado
     i = i + 1
valor = int(round(valor,2) * 100)
print("MOEDAS:")
while j < 6 :
     moedas[j] = moedas[j] * 100
     resultado = valor / moedas[j]
     print( str(int(resultado))+" moeda(s) de R$ %.2f"%(moedas[j]/100))
     resultado = valor % moedas[j]
     valor = resultado
     j = j + 1
