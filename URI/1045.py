a, b, c = map(float, input().split())

if(a >= (b+c) or b >= (a+c) or c >=(a+b)):
    print("NAO FORMA TRIANGULO")
elif((a**2) == ((b**2)+(c**2)) or (b**2) == ((a**2)+(c**2)) or (c**2) == ((a**2)+(b**2))):
    print("TRIANGULO RETANGULO")
elif((a**2) > ((b**2)+(c**2)) or (b**2) > ((a**2)+(c**2)) or (c**2) > ((a**2)+(b**2))):
    print("TRIANGULO OBTUSANGULO")
elif((a**2) < ((b**2)+(c**2)) or (b**2) < ((a**2)+(c**2)) or (c**2) < ((a**2)+(b**2))):
    print("TRIANGULO ACUTANGULO")
if(a == b and a == c):
    print("TRIANGULO EQUILATERO")
if((a == b != c) or (a == c != b) or (b == c != a)):
    print("TRIANGULO ISOSCELES")
