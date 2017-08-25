lista = list(range(100))
a = float(input())
for i in range(len(lista)):
    lista[i] = a
    print("N[%d] = %.4f"%(i, lista[i]))
    a*= 0.5
