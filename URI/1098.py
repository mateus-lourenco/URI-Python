i = 0
j = 1
while i <= 2:
    print("I=%d J=%d"%(i,j))
    print("I=%d J=%d"%(i,(j+1)))
    print("I=%d J=%d"%(i,(j+2)))
    if i != 2:
        print("I=%.1f J=%.1f"%((i+0.2),(j+0.2)))
        print("I=%.1f J=%.1f"%((i+0.2),(j+1+0.2)))
        print("I=%.1f J=%.1f"%((i+0.2),(j+2+0.2)))
        
    j+=1
    i+=1
    
