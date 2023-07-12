#Com isto consigo cortar as strings de maneira rapida para dividir as sentenças
#A contagem sempre inicia em 0
#[start:stop:step]

name = "Gustavo Goetten"

first_name = name[0:7] #eu tmb poderia colocar apenas [:7] que daria o mesmo resultado
last_name = name[8:15] #eu tmb poderia colocar apenas [8:] que daria o mesmo resultado
funcky_name = name[0:15:3] #intercala de acordo com o numero que eu colocar
reversed_name = name [::-1]

print(first_name)
print(last_name)
print(funcky_name)
print(reversed_name)

# other exemples

website1 = "https://github.com/GustavoG0etten."
website2 = "https://github.com/Jorge."

slice = slice(19,-1)

print(website1[slice])
print(website2[slice])


