def validar(f):
    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError("X ou Y não podem ser negativos")
        return f(x, y)
    return valida


@validar
def soma(x, y):
    return x + y


print(soma(10, -20))
