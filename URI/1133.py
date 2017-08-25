x  = int(input())
y  = int(input())

maior = x if x > y else y
menor = y if y < x else x
menor+=1
while menor < maior :
    if (menor % 5 == 2 or menor % 5 == 3):
        print(menor)
    menor+=1
