def listToMatrix(dna):
    dna2 = ''
    W = []
    indice = 0

    # a partir del la longitud del primer elemento de la lista obtengo el
    # tamano de la matriz
    numero_filas = len(dna[0])

    # genero un string a partir de la lista
    for i in range(len(dna)):
        dna2 = dna2 + dna[i]
        i = i + 1

    # inserto un espacio entre todas las letras
    dna_list = " ".join(dna2).split()

    # armo la matriz
    for i in range(numero_filas):
        W.append(dna_list[indice:indice + numero_filas])
        indice = indice + numero_filas

    return W


def secuencia(lista=[]):
    ''' Devuelve true si la secuencia es valida y la letra de la secuencia '''
    actual = lista[0]
    se_repite = 0
    es_secuencia = False

    for i in range(len(lista)):
        if actual == lista[i]:
            se_repite = se_repite + 1
            if se_repite == 4:
                es_secuencia = True
                break
        else:
            se_repite = 0
            actual = lista[i]

    return es_secuencia, actual


def dna_valido(dna):
    ''' 
        Devuelve true si dna cumple con las condiciones 
        de la base nitrogenada del ADN 
    '''
    es_valida = True
    if len(dna) >= 4:
        for i in range(len(dna)):
            if len(dna) != len(dna[i]):
                es_valida = False
            else:
                for j in range(len(dna[i])):
                    if dna[i][j] not in 'ACGT':
                        es_valida = False
                        break
    return es_valida


def listasIguales(x, y):
    son_iguales = True
    if len(x) != len(y):
        son_iguales = False
    else:
        for i in range(len(x)):
            if(x[i] != y[i]):
                son_iguales = False
    return son_iguales