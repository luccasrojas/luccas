import collatz_modulo as mod
def info_app():
    print('Bienvenido al programa sobre la conjetura de Collatz')
    print('A partir de un numero se puede siempre llegar a 1')
    print('Este programa puede mostrar los pasos y el numero de pasos que se deben realizar para poder lograr esto')
def iniciar_app():
    info_app()
    x=1
    while not x==3:
        print('1. Para mostrar los pasos')
        print('2. Para mostrar el numero de pasos')
        print('3. Para salir de la aplicacion')
        x=int(input('Eliga una opcion: '))
        if x==1:
            y=int(input('Cual es el numero que desea: '))
            mod.mostrar_pasos(y)
        elif x==2:
            y=int(input('Cual es el numero que desea: '))
            mod.contar_pasos(y)
        elif x==3:
            print('La aplicacion se cerro')
        else:
            print('\nLa opcion no es valida, porfavor ingrese una opcion valida: \n')
iniciar_app()