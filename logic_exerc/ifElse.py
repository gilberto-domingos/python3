name = str(input('Qual é o seu nome?'))
if name == 'Leandro':
 print('Esse nome é mais legal!')
elif name == 'Mario' or name == 'Maria' or name == 'Paulo':
    print('Seu nome é bem popular no brasil')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}'.format(name))

x = int(input("Insira um número inteiro: "))

# exemplo com inteiros

if x < 0:
    x = 0
    print('Negativo alterado para zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Um')
else:
    print('Maior')