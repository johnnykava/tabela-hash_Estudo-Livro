import Tabela_ASCII as ASCII

def setHash(nome, valor, tamanho_vetor, array):
    posicao_vetor = ASCII.EncontraASCII(nome) % tamanho_vetor

    if(array[posicao_vetor] is None):
        array[posicao_vetor] = (nome, valor)
        return
    else:
        for i in range(1, len(array)):
            posicao_quadrada = (posicao_vetor + (i ** 2)) % tamanho_vetor
            if(array[posicao_quadrada] is None):
                array[posicao_quadrada] = (nome, valor)
                return


def getHash(nome, tamanho_vetor, array):
    posicao_vetor = ASCII.EncontraASCII(nome) % tamanho_vetor

    if(array[posicao_vetor] is not None and array[posicao_vetor][0] == nome):
        print(array[posicao_vetor])
        return
    else:
        for i in range(len(array)):
            posicao_quadrada = (posicao_vetor + (i ** 2)) % tamanho_vetor
            if(array[posicao_quadrada] is not None and array[posicao_quadrada][0] == nome):
                print(array[posicao_quadrada])
                return

    