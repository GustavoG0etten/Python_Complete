# Loop alinhados
# Montar um retangulo usando certas letras

rows = int(input('Quantas linhas? '))
columns = int(input('Quantas colunas? '))
symbol = input('Coloque o simbolo que será utilizado: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print('')


