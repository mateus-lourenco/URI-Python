x  = int(input())
y  = int(input())

maior = x if x > y else y
menor = y if y < x else x
soma = 0
while menor <= maior :
    if (menor % 13 != 0 or menor % 13 != 0):
        soma += menor
    menor+=1
print(soma)
