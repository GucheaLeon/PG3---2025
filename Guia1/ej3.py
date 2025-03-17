def pintame(ancho, alto, caracter):
    for i in range(alto):
        print(caracter * ancho)

    return
ancho=(int(input("ancho de un rectangulo")))
alto=(int(input("alto de un rectangulo")))
caracter=(input("caracter que se escribe"))
pintame(ancho, alto, caracter)
