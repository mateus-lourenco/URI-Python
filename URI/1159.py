parada = True

while parada:
    x = int(input())
    soma = 0    
    i = 1
    
    if x == 0:
        break
        
    while i <= 5:
        if x % 2 == 0:
            soma += x
            x += 2
        else:
            x += 1
            i-=1
        i+=1
    print(soma)
        

    
