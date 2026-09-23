# -*- coding: utf-8 -*-
"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""

def main():
    
    d = dict()
    
    with open("LaCelestina.txt", encoding = "UTF-8") as f:
        linea = f.readline()
        
        while linea: #siempre que linea no sea vacía = TRUE si linea vacía = FALSE
            separado = linea.split() #obtengo las palabras de una linea.
          
            for palabra in separado:
                palabra = palabra.lower().strip(".,;:!?¡¿()[]\"'") #estandarizar palabra
                
                if palabra not in d:
                        d[palabra] = 1
                else:
                        d[palabra] += 1  
                        
            linea = f.readline()
            
    f.close()
    print(d)
        
    
if __name__ == "__main__":
    main()