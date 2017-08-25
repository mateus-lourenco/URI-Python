limite = int(input())
i = 1


while i <= limite :
    
    soma = 0
    j = 1
    
    x, y= map(int, input().split())
    
    if(x % 2 == 0):
        x+=1
        
    while j <= y:
        
        soma +=x
        x += 2
        j += 1
        
    print(soma)
    
    i+=1  
    

    
