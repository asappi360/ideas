# -*- coding: utf-8 -*-
"""
DOMINANDO COMPRESIONES:
    
    Ejercicio 1:  
        Tienes este diccionario:

precios = {"manzana": 1.2, "pera": 1.5, "naranja": 1.1}
Crea un diccionario donde las claves estén en mayúsculas y los valores sean céntimos (en vez de euros):

python
# resultado esperado (aprox):
    # resultado esperado (aprox):
{"MANZANA": 120, "PERA": 150, "NARANJA": 110}

"""
###PSEUDOCÓDIGO:
#crear diccionario nuevo
#coger items() iterar sobre x, y (clave) (valor). 
#aplicar los cambios deseados a clave, valor.
# guardar los cambios

#FORMA DESARROLLADA:
    
precios = {"manzana": 1.2, "pera": 1.5, "naranja": 1.1}
res = dict()

for clave, valor in precios.items():
    nueva_clave = clave.upper()
    nuevo_valor = int(valor * 100)
    
    res[nueva_clave]=nuevo_valor
    
#FORMA COMPRESIÓN:
    
    precios_compresion =  {"manzana": 1.2, "pera": 1.5, "naranja": 1.1}
    res_compresion = dict()
    
    nuevo = {clave.upper() : valor * 100 for clave, valor in precios_compresion.items()}
    
"""
DOMINANDO COMPRESIONES:
    
    Ejercicio 2
Dado:
texto = "Hola, mundo! Python 3.11 es genial :)"

Crea una cadena con solo letras y números
Crea una cadena con solo vocales
Crea una lista con todas las palabras en minúsculas, sin signos de puntuación.

"""
texto = "Hola, mundo! Python 3.11 es genial :)"
###PSEUDOCÓDIGO:
#crear variable str() vacía, comprobar que es isalnum(), si lo es: añadir a variable.

str_alnum = "".join(char for char in texto if char.isalnum())
str_aeiou = "".join(vocal for vocal in texto if vocal in "aeiou")

#FORMA DESARROLLADA:
limpio = ""
for c in texto: 
    if c.isalnum() or c.isspace():
        limpio += c
        
#FORMA COMPRESIÓN:
palabra = "".join(c if c.isalnum() or c.isspace() else " " for c in texto).lower().split()
    
###CONCLUSIÓN: pueden haber formateos o condiciones al inicio y después de
###declarar la variable en la que trabaja el bucle.

### X FOR X IN VARIABLE
### X IF condicion OR condicion (se añaden) ELSE (sino tal) cambio FOR X in VARIABLE

"""
DOMINANDO COMPRESIONES:
    
        Ejercicio 3

Tienes:

lineas = ["  Hola mundo  \n", "\tPython es genial  ", "  Compresiones de listas  \n"]
Crea una lista con las líneas sin espacios al principio/fin ni saltos de línea:

Crea una lista con las líneas en mayúsculas y sin espacios extra:


"""

lineas =["  Hola mundo  \n", "\tPython es genial  ", "  Compresiones de listas  \n"]

res_lineas = [linea.strip() for linea in lineas]

res_lineas_dos = [char.split() for char in res_lineas]





































