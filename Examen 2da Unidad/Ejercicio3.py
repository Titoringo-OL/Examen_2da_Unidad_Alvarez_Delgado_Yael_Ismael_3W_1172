# Ejercicio 3                                                                                       
"""
Escribir un programa que almacene las
asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
"""
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Definimos una lista de materias
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Creamos un diccionario para almacenar las notas
notas = {}

# Iteramos sobre cada asignatura para preguntar por la nota
for materia in materias:
    # Pedimos al usuario que introduzca la nota para la asignatura actual
    nota = input(f"Introduce la nota que has sacado en {materia}: ")
    # Almacenamos la nota en el diccionario
    notas[materia] = nota

# Mostramos las asignaturas y sus respectivas notas
print("\nResultados:")
for materia, nota in notas.items():
    print(f"En {materia} has sacado {nota}")
