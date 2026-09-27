# -*- coding: utf-8 -*-
"""
/* 
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
 
"""
import unicodedata
import re

diccionario = dict()
diccionario[" "] = "|" #entre letras
diccionario["  "] = ". . . . ." #entre palabras
diccionario["A"] = ". _"
diccionario["B"] = "_ . . ."
diccionario["C"] = "_ . _ ."
diccionario["D"] = "_ . ."
diccionario["E"] = "."
diccionario["F"] = ". . _ ."
diccionario["G"] = "_ _ ."
diccionario["H"] = ". . . ."
diccionario["I"] = ". ."
diccionario["J"] = ". _ _ _"
diccionario["K"] = "_ . _"
diccionario["L"] = ". _ . ."
diccionario["M"] = "_ _"
diccionario["N"] = "_ ."
diccionario["O"] = "_ _ _"
diccionario["P"] = ". _ _ ."
diccionario["Q"] = "_ _ . _"
diccionario["R"] = ". _ ."
diccionario["S"] = ". . ."
diccionario["T"] = "_"
diccionario["U"] = ". . _"
diccionario["V"] = ". . . _"
diccionario["W"] = ". _ _"
diccionario["X"] = "_ . . _"
diccionario["Y"] = "_ . _ _"
diccionario["Z"] = "_ _ . ."

morse_a_letra = {valor: clave for clave, valor in diccionario.items()}

frase = "Hace un buen día para estar en Vulture"
codigo = ". . . .|. _|_ . _ .|.|  . . _|_ .|  _ . . .|. . _|.|_ .|  _ . .|. .|. _|  . _ _ .|. _|. _ .|. _|  .|. . .|_|. _|. _ .|  .|_ .|  . . . _|. . _|. _ . .|_|. . _|. _ .|.|  "

def normalizar(frase):
    nfkd = unicodedata.normalize('NFD', frase)
    sin_acentos = ''.join(c for c in nfkd if unicodedata.category(c) != 'Mn')
    
    # Recorre cada carácter c en nfkd   
    # Se queda solo con los caracteres que NO son marcas diacríticas (acentos)
    # Une todos esos caracteres en una cadena nueva
    
    return sin_acentos.upper()


def a_morse(frase:str) -> str:
    aux = ""  # frase traducida completa
    
    for palabra in frase.split():      # bucle de palabras
        aux2 = ""                      # traducción de una palabra

        for letra in palabra:          # bucle de letras
            if letra in diccionario:   # HACE  UN  BUEN  ...
                aux2 += diccionario[letra] + "|"
            else:
                aux2 += "? "

        aux += aux2 + "  "             # doble espacio entre palabras

    return aux


def a_natural(codigo:str) -> str:  
    aux = "" # traducción
    # palabras = codigo.split("  ")
    # letras = palabras.split("-. ")
    
    for string in codigo.split("  "):
        aux2= ""
        for cod in string.split("|"):
            if cod in morse_a_letra.keys():
                aux2 += morse_a_letra[cod]
            else:
                aux2 += " "
        aux += aux2
        
    return aux

def natural_regex(frase:str) -> bool:
    if not isinstance(frase, str):
        raise TypeError("El parámetro de la cadena debe ser str")
    
    natural = r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ¿¡.,;:!?()\-\s]+$"
    prueba = bool(re.match(natural, frase))
    
    return prueba

def morse_regex(frase:str) -> bool:
    if not isinstance(frase, str):
        raise TypeError("El parámetro de la cadena debe ser str")
        
    morse = r"^[-._ |]+$"
    prueba = bool(re.match(morse, frase))
    
    return prueba

def traduccion(frase:str) -> str:
    mensaje = ""
    aux=""
    if natural_regex(frase):
        aux = normalizar(frase)
        mensaje = a_morse(aux)

    else:
        if morse_regex(frase):
            mensaje = a_natural(frase)
        
    return mensaje

# print(detectar(frase))
# print(detectar(codigo))
# print(a_morse(normalizar(frase)))
# print(a_natural(a_morse(normalizar(frase))))
# print(detectar(codigo))

print(traduccion(frase))
print(traduccion(codigo))
