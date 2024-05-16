'''
Timelimit: 1
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias.
'''
# Leitura do valor de entrada
N = int(input("Digite um dos valores disponíveis :"))

# Definição das cédulas disponíveis
cedulas = [100, 50, 20, 10, 5, 2, 1]

# Armazenar a quantidade de cada cédula necessária
quantidade_cedulas = []

# Valor inicial
valor = N

# Cálculo da quantidade de cada cédula
for cedula in cedulas:
    quantidade = valor // cedula
    quantidade_cedulas.append(quantidade)
    valor -= quantidade * cedula

# Impressão do valor lido
print(N)

# Impressão da quantidade de cada cédula
for i in range(len(cedulas)):
    print(f"{quantidade_cedulas[i]} nota(s) de R$ {cedulas[i]},00")
