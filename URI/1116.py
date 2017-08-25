n = int(input())
i = 1
div = 0
while i <= n:
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        div = x / y
        print("%.1f"%div)     
    i+=1
