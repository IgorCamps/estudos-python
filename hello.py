#-*- coding: utf-8 -*-

"""
#Conhecendo a função print

print ("Olá mundo!")

#Operações matemáticas

print (2 + 2)
print (2 - 2)
print (2 * 2)
print (2 / 2)
print (2 **2)
print (2 % 2)

#Variaveis

minha_variavel = "Olá mundo!"
print (minha_variavel)

#Atribuição

var1 = 1 #variável inteira
var2 = 1.1 #variavel float
var3 = "Eu sou uma string" #variável string
var4 = True #verdadeiro
var4 = False #falso

print (var1)
print (var2)
print (var3)
print (var4)

#Operadores Relacionais

x = 2
y = 3

soma = x + y

print (soma < y)


#Operadores Lógicos

x = 3
y = 3
z = 4

print (x == y or  x == z and z == y)


#Comandos Condicionais

x = 1
y = 2

if x > y: 
    print ("x é maior que y")
if y > x:
    print("y é maior que x")


#Comando else e elif

x = 1
y = 2

if x>y:
    print("x maior que y")
elif y > x:
    print("y maior que x")
else:
    print("numero iguais")


#Laços de Repetição

x = 1 

while x < 10: 
    print (x)
    x *= 3


#Laço para varrer uma lista/conjunto de elementos

lista1 = [1,2,3,4,5]
lista2 = ["Ola", "mundo", "!"]
lista3 = [0, "ola", "biscoito", "bolacha", 9.99, True]

for i in lista2:
    print(i)

#Começa em 10, conta até 20 e de 3 em 3
for i in range(10,20,3):
    print(i)
"""