x, y = map(int, input().split())

num = 1
cont = 0
i = 1
saida = ""

while i <= y :
    
	if cont < x :
		saida += str(num) + " "
		cont += 1
		num +=1
	else :
		print(saida.strip())
		saida = ""
		cont = 0
		i -= 1
	i += 1
print(saida.strip())
