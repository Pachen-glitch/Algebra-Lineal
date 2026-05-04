import numpy as np
class GaussJordan:
    def __init__(self,ecuaciones):
        self.x = ecuaciones     #MATRIZ
    
    def resolver(self):
        x = self.x              #MATRIZ
        m = len(x)              #CANTIDAD DE ECUACIONES
        n = len(x[0])-1           #CANTIDAD DE VARIABLES
        if self.verificar1(m,n): raise Exception("","")
    
    
#================== CASOS ESPECIALES ==================
    
    #CASO 1: Más variables que ecuaciones
    def verificar1(self,m,n):
        return m<n