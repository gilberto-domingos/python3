'''
Uma loja A deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000).  Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento da loja B. Caso a loja A não tenha faturado mais que a loja B, então mostre a mensagem "Loja A não superou o faturamento da loja B".
'''

faturamentoLojaA = 0
faturamentoLojaB = 54000
i = 1
while i < 5:
    fatura = int(input("Digite o valor da fatura do cliente {}:".format(i+1)))
    faturamentoLojaA += fatura
    i += 1
if (faturamentoLojaA > faturamentoLojaB):
    print("A loja A faturou {} a mais que a loja B".format(
        faturamentoLojaA-faturamentoLojaB))
else:
    print("A Loja A não superou o faturamento da Loja B.")
