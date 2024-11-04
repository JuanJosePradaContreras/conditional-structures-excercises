#Ejercicio 5

def ordenar_numeros():
    # Solicitar los cinco números al usuario
    numeros = []
    for i in range(5):
        num = int(input(f"Introduce el número {i + 1}: "))
        numeros.append(num)
    
    # Ordenar los números
    numeros.sort()
    
    # Mostrar los números ordenados
    print("Los números ordenados de menor a mayor son:", ", ".join(map(str, numeros)))

ordenar_numeros()