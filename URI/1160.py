limite = int(input())
i = 1
while i <= limite:
    pa, pb, g1, g2 = map(float, input().split())
    anos = 0
    sec = 0
    while pa <= pb:
        pa+= int(pa*g1/100)
        pb+= int(pb*g2/100)
        anos+=1
        if anos > 100:
            sec = 1
            break
    if sec == 0:
        print("%d anos."%anos)
    else:
        print("Mais de 1 seculo.")
    i+=1
