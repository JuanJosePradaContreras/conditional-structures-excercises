#Ejercicio 6

#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, 
#determine si es mayúscula o minúscula.

def clasificar_caracter():
    
    caracter = input("Introduce a character: ")

    
    if len(caracter) != 1:
        print("Please, introduce a character")
        return

    if caracter.isalpha():
        if caracter.isupper():
            print(f"The character '{caracter}' is a capital letter")
        else:
            print(f"The character '{caracter}' is a lowercase letter.")
    elif caracter.isdigit():
        print(f"The character '{caracter}' is a number.")
    else:
        print(f"The character '{caracter}' isn't a letter and a number.")

clasificar_caracter()