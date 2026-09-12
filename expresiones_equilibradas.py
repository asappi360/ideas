# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:07:55 2026
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""

def lectura(texto:str)->dict:
    delimitadores = list("[]{}()")
    conteo = dict()
    
    for char in texto.strip():
        
        if char in delimitadores:
            
            if char not in conteo:
                conteo[char] = 1
            else:
                conteo[char] += 1
    
    return conteo
    
def par(lectura:dict)-> bool:
    ok = False
    total = sum(lectura.values()) # consigo pasar a int los dict.values()
    if (total % 2) == 0: 
        ok = True #si es True quiere decir que todos los delimitadores son equilibrados. Pares.
    
    return ok
            
def equilibrada(texto:str):
    
    conteo = lectura(texto)
    mensaje = f"Tu expresión : {texto} no es equilibrada"
    if par(conteo):
        mensaje =f"Enhorabuena, tu expresión: {texto} es equilibrada"
        
    return print(mensaje)

def main():
    
    texto =" { [ a * ( c + d ) ] - 5 }"
    mala = "{ a * ( c + d ) ] - 5 }"
    
    equilibrada(texto)
    equilibrada(mala)

   
if __name__== "__main__" :
    main()
