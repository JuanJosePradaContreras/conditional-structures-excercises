#Ejercicio 3

#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5

#La división no es exacta.
#Cociente: 2
#Resto: 4
#Dividendo: 100
#Divisor: 10

#La división es exacta.
#Cociente: 10
#Resto: 0

def division_exacta():
    while True:
        try:
            dividendo = int(input("Introduce the dividend: "))
            divisor = int(input("Introduce the dividend: "))
            
            if divisor == 0:
                print("The divisor can't be 0.")
                continue
            
            cociente = dividendo // divisor
            resto = dividendo % divisor
            
            if resto == 0:
                print("The division is exactly.")
            else:
                print("The division isn't exactly.")
            
            print(f"Cociente: {cociente}")
            print(f"Resto: {resto}")
            break
        
        except ValueError:
            print("Please just enter integrers.")