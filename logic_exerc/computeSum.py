'''
Exemplos de saída:
60.0
30.2
1291.0
5.1
Nenhum valor recebido.
'''

def computeSum(*args):
    if len(args) == 0:
        return "Nenhum valor recebido."

    total = sum(args)
    return total


# Exemplos de uso da função computeSum
print(computeSum(10.0, 20.0, 30.0))
print(computeSum(5.0, 25.2))
print(computeSum(6.3, 50.3, 0, 29.4, 1205))
print(computeSum(5.1))
print(computeSum())
