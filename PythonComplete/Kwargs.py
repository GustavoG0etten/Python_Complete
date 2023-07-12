# **kwargs

def hello(**kwargs):
    # print('Hello '+ kwargs['first'] + ' ' + kwargs['last'])
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')

hello(Title='Mr.', first='Antonio', middle='Alcantra', last='Neto')

















