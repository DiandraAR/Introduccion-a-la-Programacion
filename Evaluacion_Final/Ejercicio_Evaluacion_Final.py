#Escribe un programa que solicite dos números enteros a y b, y muestre 
#todos los números primos en ese rango.
def es_primo(a, b):
    for num in range(a, b + 1):  # Recorremos el rango
        if num > 1:  # Un número primo es mayor que 1
            es_primo = True
            for i in range(2, num):  # Comprobamos si tiene divisores
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(num)

# Solicitar los números al usuario
while True:
    a = int(input("Ingresa el primer número entero (a): "))
    b = int(input("Ingresa el segundo número entero (b): "))

    if a < b:
        es_primo(a,b)
        break
    else:
        print("El primer numero debe ser menor que el segundo")
        


