def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encuentra en la posición ({i}, {j})"
    return f"El valor {valor} no se encontró en la matriz"


# Definir la matriz 3x3
matriz = [
    [6, 5, 2],
    [4, 8, 9],
    [7, 3, 1]
]

# Solicitar un número al usuario
valor_buscado = int(input("Ingrese el número a buscar en la matriz: "))

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
print(resultado)
