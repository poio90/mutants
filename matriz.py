class Matriz:
    n = 0
    matriz = []

    def __init__(self, W):
        self.n = len(W)
        self.matriz = W
    
    def get_size(self):
        return self.n

    def get_fila_n(self, n):
        """ Devuelve la fila n """
        return self.matriz[n]

    def get_columna_n(self, n):
        """ Devuelve la columna n """
        columna = []
        for i in range(len(self.matriz[n])):
            columna.append(self.matriz[i][n])
        return columna

    def get_diagonal_p(self, i, k):
        """ Devuelve una diagonal de izquierda a derecha """
        # W[fila,columna]
        diagonal = []
        for j in range(self.n - i):
            # invirtiendo indice con j se otiene la diagonal inferior o viceversa
            if k < 1:
                diagonal.append(self.matriz[i + j][j])
            else:
                diagonal.append(self.matriz[j][i + j])
        return diagonal

    def get_diagonal_s(self, i, k):
        """ Devuelve una diagonal de derecha a izquierda """
        diagonal = []
        for j in range(i + 1):
            # invirtiendo indice con j se otiene la diagonal inferior o viceversa
            if k < 1:
                diagonal.append(self.matriz[i - j][j])
            else:
                diagonal.append(self.matriz[self.n - 1 - j][self.n - 1 - i + j])
        return diagonal
    
    def get_diagonales_p(self):
        diagonales = []
        for k in range(2):
            for i in range(k, self.n):
                diagonales.append(self.get_diagonal_p(i,k))
        return diagonales
    
    def get_diagonales_s(self):
        diagonales = []
        for k in range(2):
            for i in range(self.n - k):
                diagonales.append(self.get_diagonal_s(i,k))
        return diagonales

    def ver_matriz(self):
        """ Imprime la matriz """
        for i in range(self.n):
            print(self.matriz[i])
