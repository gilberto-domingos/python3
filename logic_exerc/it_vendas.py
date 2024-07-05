'''
lista de vendas representada pelo identificador "vendas". Em cada venda há um dicionário contendo a identificação da venda (id) e os itens vendidos (items). Cada item de venda possui um dicionário contendo o número identificador (prodId), a descrição (descricao) e o valor do produto (valor).
 iterar sobre a lista de vendas e analisar cada item vendido para extrair informações necessárias.
'''

venda1 = {
    'id': 1,
    'items': [
        {'prodId': 35, 'descricao': 'Mouse Pad', 'valor': 49.90},
        {'prodId': 955, 'descricao': 'Pendrive', 'valor': 89.90}
    ]
}

venda2 = {
    'id': 2,
    'items': [
        {'prodId': 4, 'descricao': 'Teclado QWERTY', 'valor': 158.50},
        {'prodId': 88, 'descricao': 'Caneta', 'valor': 15.90}
    ]
}

venda3 = {
    'id': 3,
    'items': [
        {'prodId': 8293, 'descricao': 'Notebook Tabajara', 'valor': 15890.00},
        {'prodId': 715, 'descricao': 'Geforce GTX 450', 'valor': 627.90},
        {'prodId': 52, 'descricao': 'Porta retrato', 'valor': 29.90}
    ]
}

vendas = [venda1, venda2, venda3]

# Lista para armazenar os nomes dos produtos com valor menor que 50
produtos_menor_que_50 = []

# Variável para armazenar o faturamento geral
faturamento_geral = 0.0

# Iterar sobre cada venda
for venda in vendas:
    # Iterar sobre cada item de venda
    for item in venda['items']:
        # Verificar se o valor do produto é menor que 50
        if item['valor'] < 50:
            produtos_menor_que_50.append(item['descricao'])

        # Somar ao faturamento geral
        faturamento_geral += item['valor']

# Imprimir os produtos com valor menor que 50
print("Produtos com valor menor que 50:")
for produto in produtos_menor_que_50:
    print(produto)

# Imprimir o faturamento geral formatado
print(f"Faturamento geral: {faturamento_geral:.2f}")
