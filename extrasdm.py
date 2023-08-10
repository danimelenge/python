## Ejercicios Python ##
# 1 //

var = "Estoy aprendiendo"
print(var)

# 2 //

nombre = input("Por favor, ingresa tu nombre: ")
print("¡Hola, " + nombre + "! Bienvenido/a.")

# 3 //

numero_flotante = 3.14
numero_entero = 10
texto = "Hola, Python!"

print(numero_flotante)
print(numero_entero)
print(texto)

# 4 //

# Leer dos números ingresados por el usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Determinar si los dos números son iguales
son_iguales = numero1 == numero2

# Determinar si los dos números son diferentes
son_diferentes = numero1 != numero2

# Determinar si el primero es mayor que el segundo
primero_es_mayor = numero1 > numero2

# Determinar si el segundo es mayor o igual que el primero
segundo_es_mayor_o_igual = numero2 >= numero1

# print
print("¿Los dos números son iguales?", son_iguales)
print("¿Los dos números son diferentes?", son_diferentes)
print("¿El primero es mayor que el segundo?", primero_es_mayor)
print("¿El segundo es mayor o igual que el primero?", segundo_es_mayor_o_igual)

# 5 //

cadena = input("Ingresa una cadena de texto: ")
longitud = len(cadena)
resultado = 7 <= longitud <= 10
print(resultado)

# 6 //

contrasena_guardada = "contrasena2468"  

contrasena_ingresada = input("Ingresa la contraseña: ")

if contrasena_ingresada == contrasena_guardada:
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

# 7 //

dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))

if divisor != 0:
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)
else:
    print("Error: No se puede dividir entre cero.")

# 8 //

numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")

# 9 //

edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("¡No puedes ingresar!")
else:
    print("¡Bienvenido!")

# 10 //

nombre_usuario = input("Ingrese su nombre de usuario: ")
dia_cita = input("Ingrese el día de la cita: ")
hora_cita = input("Ingrese la hora de la cita: ")
nivel_cotizacion = int(input("Ingrese su nivel de cotización (1, 2 o 3): "))

valor_pagar = nivel_cotizacion * 7000

frase = f"Señor usuario {nombre_usuario}, su cita está programada para el día {dia_cita} a las {hora_cita}, por su nivel de cotización {nivel_cotizacion} usted deberá pagar ${valor_pagar}."

print(frase)

# 11 //

def clasificar_edad(edad):
    if edad < 18:
        return "joven"
    elif edad < 65:
        return "adulto"
    else:
        return "anciano"


edad_usuario = int(input("Ingrese su edad: "))

resultado = clasificar_edad(edad_usuario)

print(f"Usted es {resultado}.")

# 12 //

ingredientes = ["harina", "azúcar", "huevos", "leche", "mantequilla", "esencia de vainilla"]

print("Lista de ingredientes:")
for ingrediente in ingredientes:
    print(ingrediente)

# 13 //

numero = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de", numero, "es:", factorial)

# 14 //

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("La temperatura en grados Fahrenheit es:", fahrenheit)

# 15 //

import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio ** 2)
print("El área del círculo es:", area)

# 16 //

