"""
Escreva um programa que receba dois números e um sinal, 
e faça a operação matemática definida pelo sinal.
"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

sinal = input("Digite a operacao: ")

if sinal == "+":
    print(num1+num2)
elif sinal == "-":
    print(num1-num2)
elif sinal == "/":
    print(num1/num2)
elif sinal == "*":
    print(num1*num2)
else:
    print("Operacao invalida")