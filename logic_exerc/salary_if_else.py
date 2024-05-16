''' A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
400.00

Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

800.01

Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %

2000.00

Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %
'''
# Leitura do valor de entrada
salario_atual = float(input("Digite o valor do salário : "))

# Determinação do percentual de reajuste
if salario_atual <= 400.00:
    percentual = 15
elif salario_atual <= 800.00:
    percentual = 12
elif salario_atual <= 1200.00:
    percentual = 10
elif salario_atual <= 2000.00:
    percentual = 7
else:
    percentual = 4

# Cálculo do valor do reajuste e do novo salário
reajuste = salario_atual * percentual / 100
novo_salario = salario_atual + reajuste

# Impressão do resultado formatado
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
