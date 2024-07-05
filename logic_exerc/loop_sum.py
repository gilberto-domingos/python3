'''
 leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + … + 1/n
'''

n = int(input("Digite o valor de N: "))
S = 0
for i in range(1, n+1, 1):
    S = S + 1/i
print(S)
