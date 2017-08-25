matriz = [0]*12
rept = 12

pos = int(input())
calc = input()
for i in range(rept):
    matriz[i] = [0] * rept
    for j in range(rept):
        valor = float(input())
        matriz[i][j] = valor
if calc.upper() == "S":
    print("%.1f"%(sum(matriz[pos])))
elif calc.upper() == "M":
    print("%.1f" %(sum(matriz[pos]) / len(matriz[pos])))
