#Ejercicio 10

#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

# 	edad < 45	edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

def calcular_riesgo(edad, imc):
    if edad < 45:
        if imc < 22.0:
            return "bajo"
        else:
            return "medio"
    else:
        if imc < 22.0:
            return "medio"
        else:
            return "alto"

def main():
    
    estatura = float(input("Ingrese su estatura en metros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))
    edad = int(input("Ingrese su edad: "))
    
    
    imc = peso / (estatura ** 2)
    
    
    riesgo = calcular_riesgo(edad, imc)
    
    
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
    print(f"Su condición de riesgo es: {riesgo}")


main()