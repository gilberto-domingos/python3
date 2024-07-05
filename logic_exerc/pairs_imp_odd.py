# conta o número de números ímpares e pares dada uma série de números:

entrada = (1, 3, 5, 9, 12, 14, 16, 18, 19, 20, 21)

impares = 0
pares = 0

for n in entrada:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Pares: {pares}')
print(f'Ímpares: {impares}')

