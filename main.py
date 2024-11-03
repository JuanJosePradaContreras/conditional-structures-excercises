#Ejercicio 4

#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.
#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol
#Palabra 1: plancha
#Palabra 2: lapices
#Las dos palabras tienen el mismo largo

def comp_words():
   
    word_1 = input("Introduce the first word: ")
    word_2 = input("Introduce the second word: ")
    
    
    lenght_1 = len(word_1)
    lenght_2 = len(word_2)
    
    
    if lenght_1 > lenght_2:
        diference = lenght_1 - lenght_2
        print(f"The word {word_1} has {diference} more characters than {word_2}.")
    elif lenght_2 > lenght_1:
        diference = lenght_2 - lenght_1
        print(f"The word {word_2} has {diference} more characters than {word_1}.")
    else:
        print("The two words has the same lenght")