matriz = [0]*12
rept = 12
coluna = []
pos = int(input())
calc = input()

for i in range(rept):
    matriz[i] = [0] * rept
    for j in range(rept):
        valor = float(input())
        matriz[i][j] = valor
for k  in range(rept):
    coluna.append(matriz[k][pos])

if calc.upper() == "S":
    print("%.1f"%(sum(coluna)))
elif calc.upper() == "M":
    print("%.1f" %(sum(coluna) / len(coluna)))
