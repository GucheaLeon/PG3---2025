def buscar_adentro(lista, nro):
    try:
        posicion=lista.index(nro)
        return print("El numero seleccionado se encuentra en la posicion",posicion)
        
    except ValueError:
        print("El numero no se encuentra en la lista")

lista=[1,2,3,4]
nro=int(input("Seleccione un valor de la lista"))
resultado=buscar_adentro(lista, nro)

