# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:20:02 2026
Palíndromos:
    /*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""


def limpieza(texto:str) -> str:
    #aprendiendo a usar generadores = (bucle, condicion) no ocupan espacio en memoria
    #. compresión =[bucle, condición] ocupan espacio en memoria.
    
    limpio = "".join(letra for letra in texto if letra.isalnum())
    limpio = limpio.lower()
    
    return limpio

def es_palindromo(limpio:str)-> bool:
     return limpio == limpio[::-1]

def palindromo(texto:str)-> bool:
    texto_limpio = limpieza(texto)
    return (es_palindromo(texto_limpio))

def main():
    
    frase = "Ana lleva al oso la avellana."
    mala = "Anaa lleva al oso la avellana"
    print(palindromo(frase))
    print(palindromo(mala))
    
if __name__ == "__main__":
    main()
    
    
  