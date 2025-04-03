# Método recursivo para calcular el determinante de una matriz cuadrada
def determinante_recursivo(matriz):
    if len(matriz) == 2:  # Caso base: matriz 2x2
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    determinante = 0
    for i in range(len(matriz)):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        signo = (-1) ** i
        determinante += signo * matriz[0][i] * determinante_recursivo(submatriz)
    return determinante

# Método iterativo para calcular el determinante de una matriz 3x3
def determinante_iterativo(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("Este método solo funciona para matrices 3x3.")
    
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    determinante = (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
    return determinante

# Ejemplo de uso
matriz = [
    [2, 3, 1],
    [4, 5, 6],
    [7, 8, 9]
]

print("Determinante (recursivo):", determinante_recursivo(matriz))
print("Determinante (iterativo):", determinante_iterativo(matriz))