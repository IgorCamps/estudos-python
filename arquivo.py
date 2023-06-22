arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

    #Imprime as linhas do arquivo
print(linhas)
    #Imprime linha por linha
for linha in linhas:
    print(linha)

    #Lê o arquivo completo
text_completo = arquivo.read()

print(text_completo)