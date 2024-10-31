#Ejercicio 1
"""
Escribir un programa que almacene las
asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura y elimine de la lista las asignaturas aprobadas. Al final el
programa debe mostrar por pantalla las asignaturas que el usuario tiene que
repetir.
"""
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")


# Lista con las materias del curso
materias = ["Ingles", "Ecosistemas", "Leoye", "Humanidades", "Pensamiento Matematico"]

def obtener_notas(materias):
    # Creamos una copia de la lista original para modificarla
    repetir_materia = materias.copy()
    
    # Recorremos cada materia para pedir la nota
    for materia in materias:
        # Pedimos al usuario que ingrese la nota
        nota = float(input(f"Ingrese la nota obtenida en {materia}: "))
        
        # Si la nota es minima a 6, la calificacion es aprobatoria
        if nota >= 6:
            repetir_materia.remove(materia)  # Eliminamos la materia si está aprobada
    
    return repetir_materia  # Devolvemos las materias que deben repetirse

if __name__ == "__main__":
    # Llamamos a la función y guardamos las materias a repetir
    repetir_materia = obtener_notas(materias)
    
    # Muestra las materias que se deben repetir o si se han aprobado todas las materias
    if repetir_materia:
        print("Materias a repetir: ")
        for materia in repetir_materia:
            print(materia)
    else:
        print("Has aprobado todas las materias")
