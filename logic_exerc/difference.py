'''
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
'''
# Leitura dos valores A, B, C e D
A = int(input("Digite o valor de A :"))
B = int(input("Digite o valor de B :"))
C = int(input("Digite o valor de C :"))
D = int(input("Digite o valor de D :"))

# Cálculo da diferença dos produtos
produto_AB = A * B
produto_CD = C * D
DIFERENCA = produto_AB - produto_CD

# Impressão do resultado formatado
print(f"DIFERENCA = {DIFERENCA}")
