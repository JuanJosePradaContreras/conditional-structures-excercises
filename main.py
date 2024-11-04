#Ejercicio 9

#El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber 
#si un set ya terminó, y quién lo ganó.

#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su 
#rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego,
# en cuyo caso el resultado final es 7-6.

#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

#si A ganó el set, o
#si B ganó el set, o
#si el set todavía no termina, o
#si el resultado es inválido (por ejemplo, 8-6 o 7-3).
#Desarrolle un programa que solucione el problema de Solarrabietas:

def estado_set(m, n):
    
    if (m >= 7 and m - n < 2) or (n >= 7 and n - m < 2) or (m > 7 and n >= 6) or (n > 7 and m >= 6):
        return "Resultado inválido"
    

    if m >= 6 and m - n >= 2:
        return "El jugador A ganó el set"
    elif n >= 6 and n - m >= 2:
        return "El jugador B ganó el set"
    elif m >= 5 and n >= 5:
        if m == 6 and n == 6:
            return "El set está en un tie-break, resultado: 7-6"
        elif m >= 7:
            return "El jugador A ganó el set"
        elif n >= 7:
            return "El jugador B ganó el set"
    else:
        return "El set todavía no ha terminado"


m = int(input("Ingrese los juegos ganados por el jugador A: "))
n = int(input("Ingrese los juegos ganados por el jugador B: "))


resultado = estado_set(m, n)


print(resultado)