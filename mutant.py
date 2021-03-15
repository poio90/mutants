from matriz import Matriz
from funciones import secuencia, listToMatrix, dna_valido


def isMutant(dna):

    es_mutante = False
    
    if dna_valido(dna):
        contador = 0
        se_repite = []

        # 1 -> listToMatrix devuelve una matriz a partir de la lista
        W = Matriz(listToMatrix(dna))


        # 2 -> recorrer las filas
        for i in range(W.get_size()):
            es_secuencia, letra = secuencia(W.get_fila_n(i))
            if es_secuencia and se_repite.count(letra) == 0:
                se_repite.append(letra)
                contador = contador + 1

        if contador > 1:
            es_mutante = True

        else:
            # 3 -> recorrer las columnas
            # W[fila,columna]
            for i in range(W.get_size()):
                es_secuencia, letra = secuencia(W.get_columna_n(i))
                if es_secuencia and se_repite.count(letra) == 0:
                    se_repite.append(letra)
                    contador = contador + 1

            if contador > 1:
                es_mutante = True

            else:
                # 4 -> comprobar diagonales diagonales
                diagonales = W.get_diagonales_p()
                for i in range(len(diagonales)):
                    if len(diagonales[i])>=4:
                        es_secuencia, letra = secuencia(diagonales[i])
                        if es_secuencia and se_repite.count(letra) == 0:
                            se_repite.append(letra)
                            contador = contador + 1
                if contador > 1:
                    es_mutante = True
                else:
                    diagonales = W.get_diagonales_s()
                    for i in range(len(diagonales)):
                        if len(diagonales[i])>=4:
                            es_secuencia, letra = secuencia(diagonales[i])
                            if es_secuencia and se_repite.count(letra) == 0:
                                se_repite.append(letra)
                                contador = contador + 1
                    if contador > 1:
                        es_mutante = True

    return es_mutante
