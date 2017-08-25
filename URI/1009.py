nome = input()
sal = float(input())
vendas = float(input())

round(sal, 2)
round(vendas, 2)

salt = (sal + (vendas * 0.15))

print("TOTAL = R$ %0.2f"%salt)
