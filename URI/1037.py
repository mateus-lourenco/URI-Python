a = float(input())

if((a < 0.00) or (a > 100.00)):
    print('Fora de intervalo')
if((a >= 0.00) and (a <= 25.00)):
    print('Intervalo [0,25]')
if((a > 25.00) and (a <= 50.00)):
     print('Intervalo (25,50]')
if((a > 50.00) and (a < 75.00)):
    print('Intervalo (50,75]')
if((a > 75.00) and (a <= 100.00)):
    print('Intervalo (75,100]')

        
