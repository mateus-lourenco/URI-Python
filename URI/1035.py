a,b,c,d = map(int, input().split())

if(b > c and d > a):
    elif((c + d) > (a + b) and (c > 0) and (d > 0) and (a % 2 == 0)):
        print("valores aceitos")
    else:
        print("valores não aceitos")

