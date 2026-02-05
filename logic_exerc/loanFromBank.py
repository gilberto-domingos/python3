# Aprovar empréstimo bancario para compra de uma casa :
# 1.Pergunte o valor da casa, 2.O salário do comprador, 3.Em quantos anos vai pagar.
# A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.

from decimal import Decimal

home = Decimal(input('Digite o valor da casa: '))
salary = Decimal(input('Digite o valor do salario do comprador: '))
years = int(input('Digite quantos anos de financiamento: '))

monthly_payment = home / (years * 12)
max_allowed = salary * Decimal('0.3')

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(home, years, monthly_payment))

if monthly_payment <= max_allowed:
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO (prestação excede 30% do salário)')


# Exemplo referência básica antiga
# preco = Decimal("19.90")
# quantidade = 3
#
# total = preco * quantidade
#
# print(f'Total: R$ {total}')

