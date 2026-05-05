import numpy as np

class GaussJordan:
    def __init__(self):
        self.x = None
        
    def nuevo(self, sistema):
        self.x = np.array(sistema, dtype=float) 
    
    def resolver(self):
        m = len(self.x)         #FILAS
        n = len(self.x[0]) - 1  #VARIABLES
        
        i = 0  # fila
        j = 0  # columna
        
        pivotes = 0
        
        # ELIMINACIÓN GAUSSIANA
        while i < m and j < n:
            
            pivot = None
            for k in range(i, m):
                if not np.isclose(self.x[k, j], 0):
                    pivot = k
                    break
            
            if pivot is None:
                j += 1
                continue
            
            if pivot != i:
                self.x[[i, pivot]] = self.x[[pivot, i]]
            
            self.x[i] = self.x[i] / self.x[i, j]
            for k in range(i+1, m):
                self.x[k] = self.x[k] - self.x[k, j] * self.x[i]
            
            pivotes += 1
            i += 1
            j += 1
        
        for fila in range(m):
            if np.allclose(self.x[fila, :n], 0) and not np.isclose(self.x[fila, n], 0):
                return 3    #NO HAY SOLUCION
        
        if pivotes < n:
            return 2    #INFINITAS SOLUCIONES
        
        # GAUSS-JORDAN
        for i in range(m-1, -1, -1):
            pivot_col = None
            for j in range(n):
                if not np.isclose(self.x[i, j], 0):
                    pivot_col = j
                    break
            
            if pivot_col is None:
                continue
            
            for k in range(i):
                factor = self.x[k, pivot_col]
                self.x[k] = self.x[k] - factor * self.x[i]
            
        return 1 # SOLUCION UNICA