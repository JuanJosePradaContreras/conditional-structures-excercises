#Ejercicio 10

#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros 
#dos.

#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.

def tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "El triángulo es inválido."
    
    
    if a == b == c:
        return "El triángulo es equilátero."
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles."
    else:
        return "El triángulo es escaleno."


a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))


resultado = tipo_triangulo(a, b, c)


print(resultado)