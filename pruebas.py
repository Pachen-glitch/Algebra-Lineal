import GaussJordan as gauss
import numpy as np

def formato(x):
    x=x.split(';')
    x=np.array([list(map(int,i.split())) for i in x])
    return x

subs = "₀₁₂₃₄₅₆₇₈₉"

def subindice(num):
    return ''.join(subs[int(d)] for d in str(num))


gg=gauss.GaussJordan()
while True:
    x = input("Matriz: ")
    if x=='s': break
    x = formato(x)
    print(x)
    gg.nuevo(x)
    e=gg.resolver()
    if e==1:
        sol = gg.x[:,-1]
        for i in range(len(sol)):
            print(f"x{subindice(i+1)} = {sol[i]}")
    if e==2:
         print("Infinitas soluciones")
        
    if e==3:
         print("Infinitas soluciones")
    
    print()