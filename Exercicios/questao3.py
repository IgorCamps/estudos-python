"""
Escreva um programa que resolva uma 
equação de segundo grau
"""

a = 2
b = 8 
c = -24

delta = (b*b) - (4 * (a)*(c))

x1 = (-b - (delta**(1/2)))/ (2*a)
x2 = (-b + (delta**(1/2)))/ (2*a)

print(x1)
print(x2)