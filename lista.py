"""
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

#print(minha_lista[2])

#print(minha_lista)
#print(minha_lista2)
#print(minha_lista3)

#for item in minha_lista:
 #   print(item)

#tamanho = len(minha_lista)
#print(tamanho)

#Adicionando elementos

minha_lista.append("limao")
print(minha_lista)

#verificar se está na lista
if 3 in minha_lista2:
    print("3 esta na lista")

#remover elemento da lista

del minha_lista[:]
print(minha_lista)

#criar lista em branco
minha_lista4 = []

minha_lista4.append(57)
print(minha_lista4)

"""

#Ordenar lista

lista = [124,345,5,72,46,6,7,3,1,7,0]
lista2 = ["bola", "abacate", "dinheiro"]

lista2.sort()
#sort altera a lista original
#lista.sort()

#caso eu queira reverter a lista
#lista.sort(reverse=True)

#deixar a lista ao contrário
lista.reverse()

#altera a lista que já existe
#lista = sorted(lista)
print(lista)
print(lista2)