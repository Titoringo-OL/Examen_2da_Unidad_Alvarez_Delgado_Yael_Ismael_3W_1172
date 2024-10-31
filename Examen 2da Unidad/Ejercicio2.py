# Ejercicio 2
"""
Escribir un programa que almacene el diccionario
con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y
después muestre por pantalla los créditos de cada asignatura en el
formato <asignatura>
tiene <créditos> créditos, donde <asignatura> es
cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe
mostrar también el número total de créditos del curso.
"""
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Definir el diccionario con los créditos de las asignaturas
creditos_materias = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

# Mostrar los créditos de cada asignatura
for asignatura, creditos in creditos_materias.items():
    print(f"{asignatura} tiene {creditos} créditos")

# Calcular el número total de créditos del curso
total_creditos = sum(creditos_materias.values())
print(f"Numero total de créditos del curso: {total_creditos}")



