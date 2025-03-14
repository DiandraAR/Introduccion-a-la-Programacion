def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


# Definir la matriz 3x3
matriz = [
    [6, 5, 2],
    [8, 9, 4],
    [7, 3, 1]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definir la fila a ordenar
fila_a_ordenar = 2  # Tercera fila (índice 2)
bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila seleccionada
print("\nMatriz después de ordenar la fila 3:")
for fila in matriz:
    print(fila)
