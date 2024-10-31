# Ejercicio 4
"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y
teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
mensaje <nombre> tiene
<edad> años, vive en <dirección> y su número de teléfono es
<teléfono>.
"""

print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Creamos un diccionario para almacenar la información del usuario
usuario = {}

# Pedimos al usuario que introduzca su nombre
usuario['nombre'] = input("Introduce tu nombre: ")

# Pedimos al usuario que introduzca su edad
usuario['edad'] = input("Introduce tu edad: ")

# Pedimos al usuario que introduzca su dirección
usuario['direccion'] = input("Introduce tu dirección: ")

# Pedimos al usuario que introduzca su número de teléfono
usuario['telefono'] = input("Introduce tu número de teléfono: ")

# Mostramos la información del usuario en un formato específico
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
