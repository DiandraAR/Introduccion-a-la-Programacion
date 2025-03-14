# Definir las ciudades y los días de la semana
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear la matriz 3D con temperaturas distintas
temperaturas = [
    [  # Quito
        [30, 32, 31, 29, 28, 27, 26],  # Semana 1
        [25, 27, 26, 28, 29, 30, 31],  # Semana 2
        [32, 33, 35, 36, 34, 30, 29],  # Semana 3
        [28, 29, 27, 26, 30, 32, 31]  # Semana 4
    ],
    [  # Guayaquil
        [15, 18, 20, 22, 21, 19, 17],  # Semana 1
        [16, 19, 21, 23, 22, 20, 18],  # Semana 2
        [14, 17, 19, 21, 20, 18, 16],  # Semana 3
        [18, 20, 22, 24, 23, 21, 19]  # Semana 4
    ],
    [  # Cuenca
        [10, 12, 15, 14, 13, 11, 9],  # Semana 1
        [11, 13, 16, 15, 14, 12, 10],  # Semana 2
        [9, 11, 14, 13, 12, 10, 8],  # Semana 3
        [12, 14, 17, 16, 15, 13, 11]  # Semana 4
    ]
]

# Iterar sobre las ciudades y calcular el promedio de temperaturas por semana
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\n Promedios de temperatura en {ciudad}:")

    for semana_idx, semana in enumerate(temperaturas[ciudad_idx]):
        promedio = sum(semana) / len(semana)
        print(f" Semana {semana_idx + 1}: {promedio:.2f}°C")