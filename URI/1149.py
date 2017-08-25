i = 1
parada = True
while parada:
    a, n = map(int, input().split())
    soma = 0
    parada = False
    while n <= 0: n = int(input())
    
    while i <= n:
        soma += a
        a += 1
        i += 1 
    print(soma)
   
