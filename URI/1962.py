lmt = int(input())
sub = 0
i = 0
while i < lmt:
    ano = int(input())
    sub = ano - 2015
    
    if sub < 0:
        print("%d D.C."%(-sub))
    else:
        print("%d A.C."%(sub+1))
    i+=1
