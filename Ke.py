nome = input('digite seu nome: ').lower()

lista_de_palavras = nome.split()

for palavra in lista_de_palavras:
    meia_palavra = palavra [1:-1]
    ultima_letra = palavra [-1]
    primera_letra = palavra [0]
    primera_letra_maiuscula = primera_letra.upper()

    palavra_final = primera_letra_maiuscula + meia_palavra + ultima_letra

    print(palavra_final)