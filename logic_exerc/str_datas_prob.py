'''
leia um número indeterminado de valores inteiros e positivos em uma lista, encerrando a entrada de dados ao digitar o valor -1. Após a entrada de dados, mostre:
- A quantidade de números na lista: <número>
- A soma dos números da lista: <número>
- A média considerando os valores na lista: <número>
- O maior número da lista: <número>
- O menor número da lista: <número>
- Quantos números da lista são maiores que a média: <número>

calcular e exibir as estatísticas solicitadas sobre esses números. Aqui está o código para realizar essa tarefa:
'''

# Inicialização das variáveis
numeros = []
soma = 0
quantidade = 0
maior = float('-inf')
menor = float('inf')
maiores_que_media = 0

# Entrada de dados
while True:
    valor = int(input("Digite um número inteiro positivo (-1 para encerrar): "))
    if valor == -1:
        break
    if valor >= 0:
        numeros.append(valor)
        soma += valor
        quantidade += 1
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

# Cálculo da média
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

# Contagem de números maiores que a média
for num in numeros:
    if num > media:
        maiores_que_media += 1

# Saída dos resultados
print(f"A quantidade de números na lista: {quantidade}")
print(f"A soma dos números da lista: {soma}")
print(f"A média considerando os valores na lista: {media:.0f}")
print(f"O maior número da lista: {maior}")
print(f"O menor número da lista: {menor}")
print(f"Quantos números da lista são maiores que a média: {maiores_que_media}")
