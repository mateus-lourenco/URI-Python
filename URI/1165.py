limite = int(input())
i = 0

while i < limite :
    
    numero = int(input())
    j = 2
    cont = 0
    
    while cont == 0 and j <= (numero**0.5):
        
        if(numero % j == 0):
            
            cont += 1
        j+=1
        
    if cont == 0:
        print("%d eh primo"%numero)
    else:
        print("%d nao eh primo"%numero)
    print("")        
    i+=1
