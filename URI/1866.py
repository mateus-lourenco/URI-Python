casos = int(input())
j = 1
s = 0
for i in range(casos):
    valor = int(input())
    if valor % 2 == 0:    
        print(0)
    elif valor % 2 != 0:
        print(1)
    
