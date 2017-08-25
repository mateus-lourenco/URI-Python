dia1 = input().split(" ")
d1 = dia1[1]
hh, mm, ss = map(int, input().split(" : "))
dia2 =  input().split(" ")
d2 = dia2[1]
hh2, mm2, ss2 = map(int, input().split(" : "))

dur = ((int(d2)* 86400) + (hh2*3600) + (mm2*60) + ss2) - ((int(d1)*86400) + (hh*3600) + (mm*60) + ss)

print("%d dia(s)"%(dur/86400))
print("%d hora(s)"%( (dur%86400) /3600) )
print("%d minuto(s)"%( ( (dur%86400) % 3600)/ 60 ) )
print("%d segundo(s)"%( ( (dur%86400)%3600) %60 ) )
