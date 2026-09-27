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

diccionario = dict()
diccionario[" "] = "-. " #entre letras
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

def normalizar(frase):
    nfkd = unicodedata.normalize('NFD', frase)
    sin_acentos = ''.join(c for c in nfkd if unicodedata.category(c) != 'Mn')
    
    # Recorre cada carácter c en nfkd   
    # Se queda solo con los caracteres que NO son marcas diacríticas (acentos)
    # Une todos esos caracteres en una cadena nueva
    
    return sin_acentos.upper()


def procesar(texto:str) -> str:
    
    texto = normalizar(texto)
    res = ""
    
    for char in texto:
        if char in diccionario:
            res += "-. " + diccionario[char]
        else:
            res += "?"
    
    
    return res

def natural(morse:str)-> str:
    res = ""
    palabras = morse.split("  ")
    for palabra in palabras:
        letras = morse.split("  ")
        
        for simbolo in letras:
            if simbolo in morse_a_letra:
                res += "-. " + morse_a_letra[simbolo]
            else:
                res += "?"  # símbolo desconocido
        
        res += " "  # espacio entre palabras
        
    return res.strip()

def traduccion(morse:str) -> str:
    traduccion = []
    for palabra in morse.split("-. "):
        
        for char in palabra:
            i = 0
            while i < len(palabra):
                i += 1
                if char in diccionario.values():
                    traduccion.append(morse_a_letra[char])
                else:
                    traduccion.append("?")
            else:
                traduccion.append("  ")
                
    return traduccion

    
# def traduccion(morse:str) -> str:

    # # traduccion = "".join(char for char in morse if char in diccionario.items())
    # traduccion = morse.split()
    # # el problema es que todos los carácteres los toma como un "." e imprime E o T "_"
    # # hay que separar las palabras de alguna forma
    # for char in morse:
    #     if char in morse_a_letra.keys():
    #          traduccion += morse_a_letra[char]
    #     else:
    #         traduccion += "?"
             
    # return traduccion

print(procesar(frase))
frase_2 = procesar(frase)
print(traduccion(frase_2))
# print(natural(frase_2))