''' Menor e Posição
Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.

Entrada
A primeira linha de entrada contem um único inteiro N (1 < N < 1000), indicando o número de elementos que deverão ser lidos em seguida para o vetor X[N] de inteiros. A segunda linha contém cada um dos N valores, separados por um espaço. Vale lembrar que nenhuma entrada haverá números repetidos.

Saída
A primeira linha apresenta a mensagem “Menor valor:” seguida de um espaço e do menor valor lido na entrada. A segunda linha apresenta a mensagem “Posicao:” seguido de um espaço e da posição do vetor na qual se encontra o menor valor lido, lembrando que o vetor inicia na posição zero.

Exemplo de Entrada	Exemplo de Saída
10
1 2 3 4 -5 6 7 8 9 10

Menor valor: -5
Posicao: 4
'''
# Leitura do valor N
N = int(input("Digite o valor N: "))

# Leitura dos valores do vetor
X = list(map(int, input().split()))

# Certifique-se de que a entrada tem exatamente N valores
if len(X) != N:
    raise ValueError(f"Esperava-se {N} valores, mas foram fornecidos {len(X)} valores.")

# Inicialização do menor valor e sua posição
menor_valor = X[0]
posicao = 0

# Percorrer o vetor para encontrar o menor valor e sua posição
for i in range(1, N):
    if X[i] < menor_valor:
        menor_valor = X[i]
        posicao = i

# Impressão do menor valor e sua posição
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
