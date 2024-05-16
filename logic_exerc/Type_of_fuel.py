''' Timelimit: 1
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.
'''
# Inicialização dos contadores para cada tipo de combustível
alcool = 0
gasolina = 0
diesel = 0

#Códigos : 1.Álcool 2.Gasolina 3.Diesel 4.Fim

while True:
    # Leitura do código de combustível
    codigo = int(input("Digite um dos códigos acima : "))

    # Verificação do código de combustível
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        break
    # Se o código é inválido, continua o loop para solicitar um novo código
    elif codigo < 1 or codigo > 4:
        continue

# Impressão do resultado
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
