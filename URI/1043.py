lista = []
a, b, c = map(float, input().split())

lista.append(a)
lista.append(b)
lista.append(c)
d = 0
while(len(lista) == 3):
    if(a+b>c and b+c>a and a+c>b):
        perimetro = a + b + c
        print("Perimetro = %.1f"%perimetro)
        lista.append(d)
    else:
        area = (((a+b)*c) / 2)
        print("Area = %.1f"%area)
        lista.append(d)
