def mostrar_pasos(y:int):
    contador=0
    while y!=1:
        if y%2==0:
           y=y/2
        else:
           y=y*3+1
        contador=contador+1
        print(contador,'   ',y)

def contar_pasos(y:int):
    return