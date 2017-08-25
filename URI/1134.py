op = int(input())

alcool = 0
gasolina = 0
diesel = 0

while(op != 4):
    op = int(input())
    if(op == 1):
        alcool+=1
        
    elif(op == 2):
        gasolina+=1
        
    elif(op == 3):
        diesel+=1
        
    elif(op == 4):
        break

print("MUITO OBRIGADO")
print("Alcool: %d"%alcool)
print("Gasolina: %d"%gasolina)
print("Diesel: %d"%diesel)
