par = list(range(5))
impar = list(range(5))
contPar = 0
contImpar = 0
aux = 0
for j in range(15):
  valor = int(input())
  if valor % 2 == 0:
    par[contPar] = valor
    contPar+=1
    if contPar == 5:
      aux = 0
      while aux != 5:
        print("par[%d] = %d"%(aux,par[aux]))
        aux+=1
      contPar = 0
  else:
    impar[contImpar] = valor
    contImpar+=1
    if contImpar == 5:
      aux = 0
      while aux != 5:
        print("impar[%d] = %d"%(aux,impar[aux]))
        aux+=1
      contImpar = 0
  if j == 14:
    
    aux = 0
    while aux < contImpar:
      print("impar[%d] = %d"%(aux,impar[aux]))
      aux+=1
      
    aux = 0
    while aux < contPar:
      print("par[%d] = %d"%(aux,par[aux]))
      aux+=1
    
    
    
  
