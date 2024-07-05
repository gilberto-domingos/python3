nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome} é adulto")
else:
    print(f"{nome} não é adulto")

'''
if idade <= 10:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
'''