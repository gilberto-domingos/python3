'''
Timelimit: 1
Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada
Neste problema extremamente simples de repetição não há entrada.

Saída
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.
'''
# Laço de repetição de 1 a 100
for i in range(1, 101):
    # Verifica se o número é par
    if i % 2 == 0:
        # Imprime o número par
        print(i)
