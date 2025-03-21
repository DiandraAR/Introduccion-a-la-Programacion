# Definir la función para calcular la temperatura promedio de cada ciudad
def calcular_promedio_temperaturas(ciudades, temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad a partir de los datos semanales.

    Parámetros:
    ciudades (list): Lista de nombres de ciudades.
    temperaturas (list): Lista 3D de temperaturas organizadas por ciudad, semana y día.

    Retorna:
    list: Lista con los promedios de temperatura de cada ciudad.
    """
    
    promedios = []  # Lista para almacenar los promedios de cada ciudad

    # Iterar sobre cada ciudad en la lista de temperaturas
    for ciudad in temperaturas:
        suma_temperaturas = 0  # Variable para almacenar la suma total de temperaturas
        cantidad_datos = 0  # Contador para la cantidad total de datos

        # Iterar sobre cada semana dentro de la ciudad
        for semana in ciudad:
            # Iterar sobre cada día de la semana
            for temp in semana:
                suma_temperaturas += temp  # Acumular la temperatura
                cantidad_datos += 1  # Contar la cantidad de valores

        # Calcular el promedio dividiendo la suma total entre la cantidad de temperaturas
        promedio = suma_temperaturas / cantidad_datos
        promedios.append(round(promedio, 2))  # Redondear a 2 decimales y agregar a la lista

    # Crear una lista de tuplas (ciudad, promedio) para relacionar cada ciudad con su promedio
    resultado = list(zip(ciudades, promedios))  # Se evita el uso de diccionarios

    return resultado  # Retorna la lista de tuplas con los resultados


# Definir las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Crear la matriz 3D con temperaturas distintas en °C
temperaturas = [
    [  # Quito
        [30, 32, 31, 29, 28, 27, 26],  # Semana 1
        [25, 27, 26, 28, 29, 30, 31],  # Semana 2
        [32, 33, 35, 36, 34, 30, 29],  # Semana 3
        [28, 29, 27, 26, 30, 32, 31]   # Semana 4
    ],
    [  # Guayaquil
        [15, 18, 20, 22, 21, 19, 17],  # Semana 1
        [16, 19, 21, 23, 22, 20, 18],  # Semana 2
        [14, 17, 19, 21, 20, 18, 16],  # Semana 3
        [18, 20, 22, 24, 23, 21, 19]   # Semana 4
    ],
    [  # Cuenca
        [10, 12, 15, 14, 13, 11, 9],   # Semana 1
        [11, 13, 16, 15, 14, 12, 10],  # Semana 2
        [9, 11, 14, 13, 12, 10, 8],    # Semana 3
        [12, 14, 17, 16, 15, 13, 11]   # Semana 4
    ]
]

# Imprimir los resultados
print(calcular_promedio_temperaturas(ciudades, temperaturas))