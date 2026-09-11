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
 
 MEJORA PALÍNDROMO:
     
     generar de forma aleatoria una palabra (más adelante un frase de tres palabras)
     esta palabra debe existir en el diccionario de la RAE.
     Detectar si es palíndromo.
     m = 1000, n = 30, k = 10 intentos (TEORÍA DE LOS GRANDES NÚMEROS)
     sacar probabilidad de obtener un palíndromo en mil intentos
     
IDEA: 
    Detectar cuántos palíndromos existen en el diccionario RAE.
"""

def limpieza(texto:str) -> str:
    #aprendiendo a usar generadores = (bucle, condicion) no ocupan espacio en memoria
    #compresión =[bucle, condición] ocupan espacio en memoria.
    
    limpio = "".join(letra for letra in texto if letra.isalnum())
    limpio = limpio.lower()
    
    return limpio

def es_palindromo(limpio:str)-> bool:
     return limpio == limpio[::-1]

def palindromo(texto:str)-> bool:
    texto_limpio = limpieza(texto)
    return (es_palindromo(texto_limpio))

def lectura(archivo:str)->list: #MEJORA
    
    with open (archivo, "r", encoding= 'UTF-8') as f:
        contenido = f.readlines()
        return [linea.strip() for linea in contenido] #añado a una lista todas las palabras quitando los saltos de página.

def main():
    
    frase = "Ana lleva al oso la avellana."
    mala = "Anaa lleva al oso la avellana"
    print(palindromo(frase))
    print(palindromo(mala))
    
    #PARTE DE LA MEJORA
    DICCIONARIO = lectura("diccionario-rae-completo.txt")
    n = len(DICCIONARIO)
    contador = 0
    for palabra in DICCIONARIO:
        if (palindromo(palabra)):
            contador += 1
    
    probabilidad = ( contador / n ) * 100
    
    print(contador) #115 palabras que son palíndromo
    print("tienes un", probabilidad,"%", "de encontrar un palíndromo en la RAE")
    
if __name__ == "__main__":
    main()
    
    
  