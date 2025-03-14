# Definir la función para calcular la temperatura promedio de cada ciudad
def calcular_promedio_temperaturas(ciudades, temperaturas):
    promedios_por_ciudad = {}  # Diccionario para almacenar los promedios

    for i in range(len(ciudades)): # Iterar sobre cada ciudad
        total_temperaturas = 0
        cantidad_datos = 0

        for semana in temperaturas [i]:  # Iterar sobre cada semana
            for temp in semana: # Iterar sobre cada día
                total_temperaturas += temp
                cantidad_datos += 1

     # Calcular el promedio correctamente
        promedio = total_temperaturas / cantidad_datos
        # Guardar el resultado formateado con "°C"
        promedios_por_ciudad[ciudades[i]] = f"{round(promedio, 2)}°C"

    return promedios_por_ciudad
                

# Definir las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Crear la matriz 3D con temperaturas distintas en °C
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

# Imprimir los resultados
print(calcular_promedio_temperaturas(ciudades, temperaturas))