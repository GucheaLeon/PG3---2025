vocales=["a", "e", "i", "o", "u"]
contador_voc=0
def contar_vocales(frase, vocales, contador_voc):
    for i in frase:
       if(i in vocales):
        contador_voc =contador_voc+1
        
    return contador_voc


frase=input("Escriba la frase para saber la cantidad de vocales    ")
cant=contar_vocales(frase, vocales, contador_voc)
print(f"La cantidad de vocales de la frase es {cant}")

