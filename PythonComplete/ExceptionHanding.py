# exception

try:
    numerator = int(input('Escolha um numero para dividir: '))
    denominator = int(input('Escolha um numero para ser dividido: '))
    result = numerator / denominator
except ZeroDivisionError:
    print('You cant divide by zero! idiot!')
except ValueError as e:
    print(e)
    print('Enter only number plz!!')
else:
    print(result)
finally:
    print('This will always execute ')

# except Exception:
    # print('Something went wrong :(')












