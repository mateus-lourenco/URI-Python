rept = int(input())
i = 1
media = 0.0
while i <= rept:
    nota1, nota2, nota3 = map(float, input().split())
    media =( (nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2+3+5)
    print("%.1f"%media)
    i+=1
