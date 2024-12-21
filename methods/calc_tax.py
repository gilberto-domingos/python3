def calcular_taxa(faturamento: float) -> float:
    if faturamento < 1000:
        taxa = 0
    elif faturamento < 10000:
        taxa = 0.10
    elif faturamento < 500000:
        taxa < 0.15
    else:
        taxa = 0.20
    return taxa


def calcular_imposto(faturamento: float) -> float:
    taxa = calcular_taxa(faturamento)
    imposto = taxa * faturamento

    print(imposto)
    return imposto


calcular_imposto(600000)
