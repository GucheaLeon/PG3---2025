def palindromo(palabra):
    palabra = palabra.lower()  
    return palabra == palabra[::-1] 

palabra=str(input("Ingrese una palabra si desea saber si es palindromo           "))
if palindromo(palabra):
    print(f"{palabra} es un palindromo")
else:
        print(f"{palabra} no es un palindromo")
