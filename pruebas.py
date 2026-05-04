import GaussJordan as gg

def formato(x):
    x=x.split(';')
    x=[list(map(int,i.split())) for i in x]
    return x

while True:
    x = input("Matriz: ")
    if x=='s': break
    x = formato(x)
    print(x)