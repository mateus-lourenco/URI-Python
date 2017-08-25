salario = float(input())
aux = 0.0
if(salario >= 0.00 and salario <= 2000.00):
    print("Isento")
elif(salario >= 2000.01 and salario <= 3000.00):
    aux = (salario - 2000.00)* 0.08
    print("R$ %0.2f"%aux)
elif(salario >= 3000.01 and salario <= 4500.00):
    aux = ((salario - 3000.00) * 0.18) + (1000.00 * 0.08)
    print("R$ %0.2f"%aux)
else:
    aux = ((salario - 4500.00) * 0.28) + (1500.00 * 0.18) + (1000.00 * 0.08)
    print("R$ %0.2f"%aux)
