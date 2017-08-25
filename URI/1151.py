numero = int(input())
fib = list(range(47))

i = 2

fib[0] = 0
fib[1] = 1
saida = " "
saida = str(fib[0])+" "+str(fib[1])
while i < numero:
    fib[i]= fib[i-1] + fib[i-2]
    saida = saida + " " + str(fib[i])
    i+=1
print(saida)
    

    
