# (and, or, not)

temp = int(input('Qual a temperatura lá fora? '))

if temp >= 0 and temp <= 30:
    print('A temperatura está boa hoje!')
    print('Vamos lá fora!')
elif temp < 0 or temp > 30:
    print('A temperatura está ruim hoje :(')
    print('Vou assistir suits :)')

#===ou===

#Para usar not fazemos assim

if not(temp >= 0 and temp <= 30):
    print('A temperatura está boa hoje!')
    print('Vamos lá fora!')
elif not(temp < 0 or temp > 30):
    print('A temperatura está ruim hoje :(')
    print('Vou assistir suits :)')












