import Funcao_Hash as hash

tamanho_vetor = 10

lista_telefonica = [None] * tamanho_vetor

escolha = 0

while escolha != '3':
    print("---------------- MENU ----------------")
    escolha = input("1- Adicionar Pessoa\n2- Consultar Número de Telefone da Pessoa\n3- Sair\n")

    match escolha:
        case '1':
            print("----------------- Cadastro -----------------")
            nome = input("Digite o nome da pessoa que deseja colocar na lista: ")
            telefone = input("Digite o telefone de " + nome + ": ")
            
            hash.setHash(nome, telefone, tamanho_vetor, lista_telefonica)
            print("--------------------------------------------")

        case '2':
            print("----------------- Mostrando -----------------")
            nome_busca = input("Digite o nome da pessoa que deseja pesquisar na lista: ")

            hash.getHash(nome_busca, tamanho_vetor, lista_telefonica)
            print("--------------------------------------------")

        case '3':
            print("Saindo!")

        case _:
            print("Opção invalida!")