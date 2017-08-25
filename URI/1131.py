partida = 0
vinter = 0
vgremio = 0
empate = 0
parada = True
while parada:
    inter, gremio = map(int, input().split())
    resp = int(input("Novo grenal (1-sim 2-nao)\n"))

    if(inter > gremio):
        vinter+=1
    elif(gremio > inter):
        vgremio+=1
    else:
        empate+=1

    if(resp == 1):
        partida += 1
        continue
    elif (resp == 2):
        partida += 1
        parada = False
        
print("%d grenais"%partida)
print("Inter:%d"%vinter)
print("Gremio:%d"%vgremio)
print("Empates:%d"%empate)

if(vinter > vgremio):
    print("Inter venceu mais")
    
elif(vgremio > vinter):
    print("Gremio venceu mais")
    
else:
    print("Nao houve vencedor")
