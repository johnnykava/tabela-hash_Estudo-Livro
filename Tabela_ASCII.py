def EncontraASCII(nome):
    maiusculas = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 
                     77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

    nome = nome.upper()
    soma_ascii = 0

    for i in range(len(nome)):
        if nome[i] == 'A':
            soma_ascii += maiusculas[0]
        if nome[i] == 'B':
            soma_ascii += maiusculas[1]
        if nome[i] == 'C':
            soma_ascii += maiusculas[2]
        if nome[i] == 'D':
            soma_ascii += maiusculas[3]
        if nome[i] == 'E':
            soma_ascii += maiusculas[4]
        if nome[i] == 'F':
            soma_ascii += maiusculas[5]
        if nome[i] == 'G':
            soma_ascii += maiusculas[6]
        if nome[i] == 'H':
            soma_ascii += maiusculas[7]
        if nome[i] == 'I':
            soma_ascii += maiusculas[8]
        if nome[i] == 'J':
            soma_ascii += maiusculas[9]
        if nome[i] == 'K':
            soma_ascii += maiusculas[10]
        if nome[i] == 'L':
            soma_ascii += maiusculas[11]
        if nome[i] == 'M':
            soma_ascii += maiusculas[12]
        if nome[i] == 'N':
            soma_ascii += maiusculas[13]
        if nome[i] == 'O':
            soma_ascii += maiusculas[14]
        if nome[i] == 'P':
            soma_ascii += maiusculas[15]
        if nome[i] == 'Q':
            soma_ascii += maiusculas[16]
        if nome[i] == 'R':
            soma_ascii += maiusculas[17]
        if nome[i] == 'S':
            soma_ascii += maiusculas[18]
        if nome[i] == 'T':
            soma_ascii += maiusculas[19]
        if nome[i] == 'U':
            soma_ascii += maiusculas[20]
        if nome[i] == 'V':
            soma_ascii += maiusculas[21]
        if nome[i] == 'W':
            soma_ascii += maiusculas[22]
        if nome[i] == 'X':
            soma_ascii += maiusculas[23]
        if nome[i] == 'Y':
            soma_ascii += maiusculas[24]
        if nome[i] == 'Z':
            soma_ascii += maiusculas[25]

    return soma_ascii
