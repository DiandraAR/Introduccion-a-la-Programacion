# Definir la función para calcular la temperatura promedio de cada ciudad
def calcular_promedio_temperaturas(datos_temperaturas):
    """
    Esta función recibe un diccionario con los datos de temperaturas de varias ciudades a lo largo de varias semanas.
    Y retorna un diccionario con la temperatura promedio de cada ciudad.

    Parámetros:
    datos_temperaturas (dict): Diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas semanales.

    Retorno:
    dict: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}  # Diccionario para almacenar los promedios de cada ciudad

    for ciudad, temperaturas in datos_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)  # Calcular el promedio
        promedios[ciudad] = round(promedio, 2)  # Guardar el resultado redondeado a 2 decimales

    return promedios


# Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas
datos_temperaturas = {
    "Ciudad A": [60, 55, 27, 88],
    "Ciudad B": [25, 26, 49, 50],
    "Ciudad C": [18, 20, 32, 17]
}

# Llamar a la función y mostrar los resultados
promedios = calcular_promedio_temperaturas(datos_temperaturas)
print("Temperaturas promedio por ciudad:", promedios)
