'''
 implementar a função validaSenha conforme os requisitos fornecidos, verificar três condições: comprimento da senha, quantidade de números, e quantidade de caracteres maiúsculos. Vamos escrever a função com base nesses critérios:

A senha deve conter no mínimo 5 caracteres e no máximo 15 caracteres.
A senha deve conter pelo menos 2 números.
A senha deve conter pelo menos 2 caracteres em maiúsculo.
'''
password = input("Digite a sua senha :")

def validaSenha(password):
    # Verifica o comprimento da senha
    if len(password) < 5 or len(password) > 15:
        return False

    # Contadores para números e maiúsculas
    numeros = 0
    maiusculas = 0

    for char in password:
        if char.isdigit():
            numeros += 1
        elif char.isupper():
            maiusculas += 1

    # Verifica se há pelo menos 2 números e 2 maiúsculas
    if numeros >= 2 and maiusculas >= 2:
        return True

    return False


if validaSenha(password):
    print("Senha válida")
else:
    print("Senha inválida")
