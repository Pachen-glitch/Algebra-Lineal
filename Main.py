#=================================================
#       UNIVERSIDAD DEL VALLE DE GUATEMALA
#=================================================
#   Curso: Algebra Lineal 1
#   Catedrático: Rodrigo Leonardo
#   Integrantes: Daniel Leal    - 25682
#                Jorge Martínez - 25556
#                Matías Zamora  - 25760
#
#   Descripción: Programa que implementa el 
#       algoritmo de reducción de matrices
#       Gauss-Jordan.
#=================================================

import GaussJordan as gg

while True:
    x = input("Matriz: ")
    if x=='s': break
    x=x.split(';')
    x=[list(map(int,i.split())) for i in x]
    print(x)