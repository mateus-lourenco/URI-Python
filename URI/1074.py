limite = int(input())
i = 1
valores = []
j = 0
while i <= limite :
    valores.append(int(input()))
    i+=1
while j < len(valores) :
    
      if(valores[j] % 2 == 0 and valores[j] > 0):
          print("EVEN POSITIVE")
      elif(valores[j] % 2 == 0 and valores[j] < 0):
           print("EVEN NEGATIVE")
           
      if(valores[j] % 2 != 0 and valores[j] > 0):
           print("ODD POSITIVE")
      elif(valores[j] % 2 != 0 and valores[j] < 0):
           print("ODD NEGATIVE")

      if(valores[j]==0):
           print("NULL")
           
      j+=1
       
    
