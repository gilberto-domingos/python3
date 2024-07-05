'''
implemente uma função lambda que recebe 2 (dois) parâmetros "peso" e "altura". Calcule o IMC
'''

# Implementação da função lambda para calcular o IMC
getIMC = lambda peso, altura: peso / (altura * altura)

# Testando a função lambda com os exemplos fornecidos
print(getIMC(89, 1.75))
print(getIMC(75, 1.66))

'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
##########
def myfunc(n):
  return lambda a : a * n
################

mytripler = myfunc(3)

print(mytripler(11))
#############

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
##################

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

'''