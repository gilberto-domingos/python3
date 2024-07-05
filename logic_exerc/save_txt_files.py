vendas_list = [
    {
        "data": "05/02/2022",
        "valor": 1688.00,
    },
    {
        "data": "08/02/2022",
        "valor": 2006.89
    },
    {
        "data": "09/02/2022",
        "valor": 1520.00,
    },
    {
        "data": "12/02/2022",
        "valor": 54.00,
    },
]

def gravarArquivo(vendas):
    arquivo = open('files/vendas.txt', 'a')

    for v in vendas:
        arquivo.write(f"{v['data']}, {v['valor']}\n")

    # Fechamento do arquivo
    arquivo.close()

gravarArquivo(vendas_list)
