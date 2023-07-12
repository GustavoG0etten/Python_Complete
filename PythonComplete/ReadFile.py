
try:
    with open('teste.md') as file:
        print(file.read())

except FileNotFoundError:
    print('That file was not found :(')
















