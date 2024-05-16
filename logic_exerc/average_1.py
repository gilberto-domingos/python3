''' Média 1

Timelimit: 1
Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada :
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída :
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas.
'''

# Leitura dos valores A e B
A = float(input("Digite o valor de A :"))
B = float(input("Digite o valor de B :"))

# Cálculo da média ponderada
peso_A = 3.5
peso_B = 7.5
soma_pesos = peso_A + peso_B

MEDIA = ((A * peso_A) + (B * peso_B)) / soma_pesos

# Impressão do resultado formatado
print(f"MEDIA = {MEDIA:.5f}")