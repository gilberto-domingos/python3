import random
from datetime import datetime, timedelta

import pandas_local_dataframe as pd

# Fields
produtos_base = ['Notebook', 'Smartphone', 'Cadeira', 'Mesa', 'Fone de Ouvido', 'Monitor', 'Impressora', 'Teclado',
                 'Mouse', 'Câmera']
adjetivos = ['Excelente', 'Novo', 'Econômico', 'Compacto', 'Avançado', 'Confortável', 'Moderno', 'Portátil', 'Durável',
             'Elegante']
categorias_base = ['XS', 'XSS', 'XD', 'XDD', 'XF', 'XFF', 'XT', 'XTT', 'XY', 'XYY']
fabricantes_base = ['TechCorp', 'HomeFurnish', 'GadgetWorld', 'OfficeStuff', 'FashionLine', 'ToyKingdom', 'ToolMaster',
                    'SportGear', 'KitchenPro', 'AutoParts']


# Function generate itens columns
def gerar_nome_produto():
    return f'{random.choice(produtos_base)} {random.choice(adjetivos)}'


def gerar_descricao():
    return f'{random.choice(produtos_base)} {random.choice(adjetivos)} de alta qualidade'


def gerar_categoria():
    return random.choice(categorias_base)


def gerar_fabricante():
    return random.choice(fabricantes_base)


# Generate datas
produtos = [gerar_nome_produto() for _ in range(1000)]
descricoes = [gerar_descricao() for _ in range(1000)]
categorias = [gerar_categoria() for _ in range(1000)]
codigos = [str(random.randint(100000, 999999)) for _ in range(1000)]
pesos = [str(random.uniform(0.5, 20.0))[:4] + ' kg' for _ in range(1000)]
dimensoes = [f'{random.randint(10, 100)}x{random.randint(10, 100)}x{random.randint(10, 100)} cm' for _ in range(1000)]
precos = ['R$ ' + str(random.uniform(10.0, 500.0))[:5] for _ in range(1000)]
validade = [(datetime.now() + timedelta(days=random.randint(30, 365))).strftime('%d/%m/%Y') for _ in range(1000)]
tamanhos = ['P', 'M', 'G', 'GG', 'XG', 'XXG']
materiais = ['X24', 'X85', 'X65', 'X74', 'X68', 'X35']
fabricantes = [gerar_fabricante() for _ in range(1000)]
paises = ['Brasil', 'China', 'EUA', 'Alemanha', 'Japão', 'Índia']

# create DataFrame
data = {
    'Produto': produtos,
    'Descrição': descricoes,
    'Categoria': categorias,
    'Código': codigos,
    'Peso': pesos,
    'Dimensão': dimensoes,
    'Preço': precos,
    'Validade': validade,
    'Tamanho': [random.choice(tamanhos) for _ in range(1000)],
    'Material': [random.choice(materiais) for _ in range(1000)],
    'Fabricante': fabricantes,
    'País de Origem': [random.choice(paises) for _ in range(1000)]
}

df = pd.DataFrame(data)

# Save excel file
file_path = 'files/produtos_atualizados.xlsx'
df.to_excel(file_path, index=False)
print(f'Arquivo salvo como {file_path}')
