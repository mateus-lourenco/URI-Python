hora1, minuto1, hora2, minuto2 = map(int, input().split())

horas = hora2 - hora1

if(horas < 0):
    horas = 24 + horas
    
minutos = minuto2 - minuto1

if(minutos < 0):
    minutos = 60 + minutos
    horas = horas - 1
    
if(hora1 == minuto1 == hora2 == minuto2):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU "+str(int(horas))+" HORA(S) E "+str(int(minutos))+" MINUTO(S)")
