"""
Faça um programa que receba duas notas digitadas pelo usuário. Se a nota
for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 
"""

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))

media = (nota1+nota2)/2

if media>= 6.0:
    print("Aprovado",)
else:
    print("Reprovado")