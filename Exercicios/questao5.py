"""
Escreva um programa que receba dois números e um sinal, 
e faça a operação matemática definida pelo sinal.
"""

num1 = 3
num2 = 5

sinal = "/"

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