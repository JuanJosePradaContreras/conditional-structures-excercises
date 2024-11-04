#Ejercicio 7

#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.
#La salida del programa debe ser el resultado de la operación.

def calculadora():

    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        operador = input("Introduce el operador (+, -, *, /): ")

        if operador == "+":
            resultado = num1 + num2
            print(f"El resultado de {num1} + {num2} es: {resultado}")
        elif operador == "-":
            resultado = num1 - num2
            print(f"El resultado de {num1} - {num2} es: {resultado}")
        elif operador == "*":
            resultado = num1 * num2
            print(f"El resultado de {num1} * {num2} es: {resultado}")
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de {num1} / {num2} es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Operador no válido. Por favor, utiliza +, -, * o /.")
    except ValueError:
        print("Error: Por favor, introduce números válidos.")

calculadora()