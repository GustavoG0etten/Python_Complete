# Um codigo para controlar os loops

while True:
    name = input('Quan tas Lhamas: ')
    if name != '':
         break

phone_number = '99675-3508'

for i in phone_number:
    if i == '-':
        continue
    print(i, end='')

for i in range(1, 21):

    if i == 13:
        pass # Este codigo faz com que pulemos o numero 13
    else:
        print(i)
