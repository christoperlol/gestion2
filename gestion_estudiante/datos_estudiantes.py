import json
import gestion_cursos.gestion_cursos as gestion_cursos
import gestion_universidad.datos_universidad as datos_universidad

# Diccionario de estudiantes
estudiantes_dict = {}

def registrar_estudiante():
    rut = input("Ingrese el RUT del estudiante: ")
    matricula = input("Ingrese la matrícula del estudiante: ")
    nombre = input("Ingrese el nombre completo del estudiante: ")
    calificaciones = []

    for curso in gestion_cursos.cursos:
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación en {curso} (1-7): "))
                if 1 <= calificacion <= 7:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar entre 1 y 7.")
            except ValueError:
                print("Ingrese un número válido.")

    promedio = sum(calificaciones) / len(calificaciones)
    estudiantes_dict[rut] = {
        'matricula': matricula,
        'nombre': nombre,
        'calificaciones': calificaciones,
        'promedio': promedio,
        'universidad': datos_universidad.datos_universidad  # Información de la universidad
    }
    print("Estudiante registrado exitosamente.\n")

def actualizar_estudiante():
    rut = input("Ingrese el RUT del estudiante a actualizar: ")
    if rut in estudiantes_dict:
        nombre = input("Ingrese el nuevo nombre del estudiante: ")
        calificaciones = []

        for curso in gestion_cursos.cursos:
            while True:
                try:
                    calificacion = float(input(f"Ingrese la nueva calificación en {curso} (1-7): "))
                    if 1 <= calificacion <= 7:
                        calificaciones.append(calificacion)
                        break
                    else:
                        print("La calificación debe estar entre 1 y 7.")
                except ValueError:
                    print("Ingrese un número válido.")

        promedio = sum(calificaciones) / len(calificaciones)
        estudiantes_dict[rut] = {
            'matricula': estudiantes_dict[rut]['matricula'],  # Mantiene la matrícula existente
            'nombre': nombre,
            'calificaciones': calificaciones,
            'promedio': promedio,
            'universidad': datos_universidad.datos_universidad
        }
        print("Estudiante actualizado exitosamente.\n")
    else:
        print("Estudiante no encontrado.\n")

def eliminar_estudiante():
    rut = input("Ingrese el RUT del estudiante a eliminar: ")
    if rut in estudiantes_dict:
        with open("estudiantes_eliminados.json", "a") as file:
            json.dump(estudiantes_dict[rut], file)
            file.write("\n")
        del estudiantes_dict[rut]
        print("Estudiante eliminado y registro guardado.\n")
    else:
        print("Estudiante no encontrado.\n")

def visualizar_estudiantes():
    if estudiantes_dict:
        print("\nLista de Estudiantes:")
        for rut, datos in estudiantes_dict.items():
            print(f"RUT: {rut}")
            print(f"Matrícula: {datos['matricula']}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Universidad: {datos['universidad']['nombre']} - Ubicación: {datos['universidad']['ubicacion']}")
            print(f"Calificaciones: {datos['calificaciones']}")
            print(f"Promedio: {datos['promedio']:.2f}")
            print("-" * 20)
    else:
        print("No hay estudiantes registrados.\n")
        