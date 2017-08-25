limite = int(input())
i = 0

while i < limite :
    numero = int(input())
    soma = 0
    j = 1
    
    while j < numero:
        if( numero % j == 0):
            soma+=j
            if soma > numero : break
        j+=1
        
    if(soma == numero):
        print("%d eh perfeito"%numero)
    else:
        print("%d nao eh perfeito"%numero)
    i+=1
print("")
