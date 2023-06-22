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


#Strings

a = "Igor"
b = "Mariana"

concatenar = a + " " + b

print (concatenar)

#Saber tamanho da string

tamanho = len(concatenar)

print(tamanho)

#Navegação pelo índice

print(a[0])
print(a[1])
print(a[2])
print(a[3])

#Imprimindo parte de uma string

    # O primeiro valor é o que inicia e o : é para indicar até onde vai imprimir
print(concatenar[2:9])

    #Parte 2
a = "Igor"
b = "Mariana"

concatenar = a + " " + b + " "

print(concatenar)
     #Função lower()
concatenar = concatenar.lower()
print(concatenar)
     #Função upper()
concatenar = concatenar.upper()
print(concatenar)
    #Função strip()
concatenar = concatenar.strip()
print(concatenar)

    #Função split()
minha_string = "O rato roeu a roupa do rei de Roma"

#minha_string = minha_string.split("r")
#print(minha_string)   
    #Função busca/find(). Exibe o índice que a palavra está;
busca = minha_string.find("rei")
print(busca)
    #Imprimindo todo o texto da string dps da palavra "rei"
print(minha_string[busca:])
    #Se não encontra a substring, retorna -1
busca = minha_string.find("rainha")
print(busca)

    #Função replace
minha_string = minha_string.replace("o rei", "a rainha")

print(minha_string)

"""
#Funções

def soma(x,y):
    return x+y
def multiplicacao(x,y):
    return x*y

s = soma(2,3)
m = multiplicacao(3,4)

print(s)
print(m)


    #recursividade
print(soma(s,m))


#Manipulação de arquivos

