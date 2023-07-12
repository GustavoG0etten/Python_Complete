# tuple = uma lista com parenteses ao inves de colchetes

student = ('Gu', 19, 'Male')

print(student.count('Gu'))   #Quantas vezes a variavel aparece
print(student.index('Male'))   #Em qual posicao ele está

for x in student:
    print(x)

if 'Gu' in student:
    print('Gu está aqui!')



