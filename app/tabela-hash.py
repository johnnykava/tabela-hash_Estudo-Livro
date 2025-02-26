import Funcao_Hash as hash

tamanho_vetor = 10

lista_telefonica = [None] * tamanho_vetor

for i in range(4):

    print("----------------- Cadastro -----------------")
    nome = input("Digite o nome da pessoa que deseja colocar na lista: ")
    telefone = input("Digite o telefone de " + nome + ": ")

    hash.setHash(nome, telefone, tamanho_vetor, lista_telefonica)
    print("--------------------------------------------")

    print("----------------- Mostrando -----------------")
    nome_busca = input("Digite o nome da pessoa que deseja colocar na lista: ")

    hash.getHash(nome_busca, tamanho_vetor, lista_telefonica)
    print("--------------------------------------------")
