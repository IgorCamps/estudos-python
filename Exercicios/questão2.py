"""
Faça um programa que receba duas notas digitadas pelo usuário. Se a nota
for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 
"""

notas = [9.2, 5.7]

for nota in notas:
    if nota >= 6.0:
        print("Aprovado - Nota", nota)
    else:
        print("Reprovado - Nota:", nota)