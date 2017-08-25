limite = int(input())
i = 1
coelhos = 0
ratos = 0
sapos = 0
cont = 0
while i <= limite:
    string = input().split()
    if string[1] == 'C':
        coelhos += int(string[0])
    elif string[1] == 'R':
        ratos += int(string[0])
    elif string[1] == 'S':
        sapos += int(string[0])
    cont = coelhos + ratos + sapos
    i+=1
print("Total: %d cobaias"%cont)
print("Total de coelhos: %d"%coelhos)
print("Total de ratos: %d"%ratos)
print("Total de sapos: %d"%sapos)
print("Percentual de coelhos: %.2f"%(((coelhos * 100)/cont))+" %")
print("Percentual de ratos: %.2f"%(((ratos * 100)/cont))+" %")
print("Percentual de sapos: %.2f"%(((sapos * 100)/cont))+" %")
