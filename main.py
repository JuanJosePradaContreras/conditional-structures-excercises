#Ejercicio 8

#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos
#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

#Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la 
#siguiente manera (suponiendo que hoy es 11 de marzo de 2011):

#>>> from time import localtime
#>>> t = localtime()
#>>> t.tm_mday
#11
#>>> t.tm_mon
#3
#>>> t.tm_year
#2011
#El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.#

from time import localtime

def calcular_edad():
   
    t = localtime()
    dia_actual = t.tm_mday
    mes_actual = t.tm_mon
    anno_actual = t.tm_year
    
    
    dia_nacimiento = int(input("Ingrese su día de nacimiento: "))
    mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))
    anno_nacimiento = int(input("Ingrese su año de nacimiento: "))
    
   
    edad = anno_actual - anno_nacimiento
    
    
    if (mes_nacimiento > mes_actual) or (mes_nacimiento == mes_actual and dia_nacimiento > dia_actual):
        edad -= 1
    
    print(f"Usted tiene {edad} años.")


calcular_edad()