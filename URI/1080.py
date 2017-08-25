i = 0
aux = 0
pos = 0
while i <= 5:
    n = int(input())
    if n > aux:
        aux = n
        pos = i
    i+=1
print(aux)
print(pos+1)
