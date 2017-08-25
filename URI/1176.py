fib = list(range(61))
numero = int(input())
j = 2
while j <= 60:
    fib[j] = fib[j-2] + fib[j-1]
    j+=1
for i in range(numero):
    valor = int(input())
    print("Fib(%d) = %d"%(valor, fib[valor]))
    
            

    
