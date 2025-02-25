import Tabela_ASCII as ASCII

def setHash(nome, valor, tamanho_vetor, array):
    posicao_vetor = ASCII.EncontraASCII(nome) % tamanho_vetor

    print(posicao_vetor)

    array[posicao_vetor] = valor

def getHash(nome, tamanho_vetor, array):
    posicao_vetor = ASCII.EncontraASCII(nome) % tamanho_vetor

    print(posicao_vetor)

    print(array[posicao_vetor])

tamanho_vetor = 10

lista_telefonica = [None] * tamanho_vetor

for i in range(3):

    print("----------------- Cadastro -----------------")
    nome = input("Digite o nome da pessoa que deseja colocar na lista: ")
    telefone = input("Digite o telefone de " + nome + ": ")

    setHash(nome, telefone, tamanho_vetor, lista_telefonica)
    print("--------------------------------------------")

    print("----------------- Mostrando -----------------")
    nome_busca = input("Digite o nome da pessoa que deseja colocar na lista: ")

    getHash(nome_busca, tamanho_vetor, lista_telefonica)
    print("--------------------------------------------")
