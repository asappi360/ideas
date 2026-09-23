# -*- coding: utf-8 -*-
"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""
numeros = []

for num in range(51):
    numeros.append(num)

fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
i = 0

while len(fibonacci) < len(numeros):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
    i+=1
    
print(fibonacci)




#def Fibonacci(n):
    
    
