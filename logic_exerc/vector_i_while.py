''' Substituição em Vetor I

Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
'''
# Inicialização da lista
X = []

# Leitura dos 10 valores inteiros com verificação
while len(X) < 10:
    try:
        valor = int(input("Digite um número inteiro: "))
        X.append(valor)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Substituição dos valores nulos e negativos
for i in range(10):
    if X[i] <= 0:
        X[i] = 1

# Impressão do vetor atualizado
for i in range(10):
    print(f"X[{i}] = {X[i]}")
