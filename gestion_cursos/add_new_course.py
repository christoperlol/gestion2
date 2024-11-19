# Lista de cursos global compartida entre módulos
cursos = ['modelamiento de datos', 'lenguaje programacion', 'ingles', 'taller de creatividad']

def agregar_curso():
    try:
        nuevo_curso = input("Ingrese el nombre del nuevo curso: ").strip()
        if nuevo_curso:
            cursos.append(nuevo_curso)
            print(f"Curso '{nuevo_curso}' agregado exitosamente.")
        else:
            print("Error: El nombre del curso no puede estar vacío.")
    except Exception as e:
        print(f"Error al agregar curso: {e}")