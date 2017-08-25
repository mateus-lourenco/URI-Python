limite = int(input())
i = 1
while i <= limite:
    a, b = map(int, input().split())
    
    maior = a if a > b else b
    menor = b if b < a else a
    
    soma = 0
    menor += 1
    
    while menor < maior:
        if menor % 2 != 0:
            soma += menor
        menor+=1
        
    print(soma)
    i+=1

