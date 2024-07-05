def computeIMC(nome, peso, altura):
    if peso <= 0 or altura <= 0:
        return "Não foi possível calcular o IMC."

    imc = peso / (altura * altura)
    return "{} tem {} kg e {} metros de altura. O seu IMC é {:.2f}".format(nome, peso, altura, imc)


# Exemplo de uso da função
n = input("Digite o nome: ")
p = float(input("Digite o peso (kg): "))
a = float(input("Digite a altura (metros): "))

print(computeIMC(n, p, a))