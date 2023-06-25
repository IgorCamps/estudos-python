"""
Escreva um programa que resolva uma 
equação de segundo grau
"""

from math import sqrt

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2 - (4*a*c)

print(delta)

if delta < 0:
    print("Delta negativo")
else:
    raiz = sqrt(delta)
    print(raiz)
    x1 = (-b + raiz)/ (2*a)
    x2 = (-b - raiz)/ (2*a)
    
    print("Raizes: ", x1, x2)