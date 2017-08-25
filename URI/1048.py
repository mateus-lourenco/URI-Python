salario = float(input())

if(salario >= 0.00 and salario <= 400.00):
    novo = salario * 1.15
    reajuste = novo - salario
    percentual = 15    
elif(salario >= 400.01 and salario <= 800.00):
    novo = salario * 1.12
    reajuste = novo - salario
    percentual = 12
elif(salario >= 800.01 and salario <= 1200.00):
    novo = salario * 1.10
    reajuste = novo - salario
    percentual = 10
elif(salario >= 1200.01 and salario <= 2000.00):
    novo = salario * 1.07
    reajuste = novo - salario
    percentual = 7    
else:
    novo = salario * 1.04
    reajuste = novo - salario
    percentual = 4
    
print("Novo salario: %0.2f"%novo)
print("Reajuste ganho: %0.2f"%reajuste)
print("Em percentual: "+str(int(percentual))+" %")
