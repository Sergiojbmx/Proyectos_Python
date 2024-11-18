"""
    PROYECTO DEL AHORCADO
"""
from random import *
#################################################################################################################
# Función que genera una palabra random de una lista
def elegir_palabra_random():

    lista_palabras = ["inteligencia", "triangulo", "paralelepipedo", "computadora", "lluvia"]
    palabra_random = choice(lista_palabras)
    return list(palabra_random)

#######################################################################################################################
# Función para mostrar los guiones en base al numero de letras que contenga la palabra random
def mostrar_guiones(palabra):
    lista_letras = [ ]

    for letra in palabra:
        lista_letras.append("_")

    return lista_letras

#######################################################################################################################
# Función que solicita al usuario letra por letra a adivinar
def pedir_letra():
    letra = str(input("Elige una letra: "))
    while len(letra) != 1 or not letra.isalpha():
        letra = str(input("Elige nuevamente una letra: "))
    return letra

#######################################################################################################################
# Función que verifica si la letra ingresada por el usuario se encuentra en la palabra random
def validar_letra(letra, lista_letras, palabra_random):

    acierto = False

    for i in range(len(palabra_random)):
        if palabra_random[i] == letra:
            lista_letras[i] = letra
            acierto = True
    print(" ".join(lista_letras))
    return acierto

############################################################################################################
############################################################################################################
# Función principal que controla al juego y combina las funciones anteriores

def ahorcado():
    palabra = elegir_palabra_random()
    lista_letras = mostrar_guiones(palabra)
    vidas = 5

    while vidas > 0 and  "_" in lista_letras:

        print(" ".join(lista_letras))
        print(f"Te quedan {vidas} vidas")

        letra = pedir_letra()

        if not validar_letra(letra, lista_letras, palabra):
            vidas -= 1
            print("La letra que ingresaste no se encuentra, pierdes una vida")

        else:
            print("Bien hecho, continua asi!!")

    if "_" not in lista_letras:
        print("Felicidades, has adivinado toda la palabra, GANASTE!!")

    else:
        print(f"Te has quedado sin vidas. La palabra era {''.join(palabra)}")

ahorcado()





