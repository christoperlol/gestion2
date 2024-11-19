# Tupla de cursos
cursos = ('modelamiento de datos', 'lenguaje programacion', 'ingles', 'taller de creatividad')

# Importar el diccionario de estudiantes
from gestion_estudiante.gestion_estudiante import estudiantes_dict

def registrar_calificaciones():
    try:
        if not estudiantes_dict:
            print("No hay estudiantes registrados.\n")
            return

        for rut, datos in estudiantes_dict.items():
            print(f"\nEstudiante: {datos['nombre']}")
            for i, curso in enumerate(cursos):
                if i < len(datos['calificaciones']):
                    print(f"Curso: {curso}, Notas: {datos['calificaciones'][i]}")
                else:
                    print(f"Curso: {curso}, Notas: No asignadas")
            print(f"Promedio General: {datos.get('promedio', 'No calculado'):.2f}")
            print("-" * 20)
    except Exception as e:
        print(f"Error al registrar calificaciones: {e}")

def agregar_curso():
    global cursos  # Necesitamos declarar cursos como global para modificar la tupla
    try:
        nuevo_curso = input("Ingrese el nombre del nuevo curso: ")
        
        # Crear una nueva tupla con el curso agregado
        cursos = cursos + (nuevo_curso,)
        print(f"Curso '{nuevo_curso}' agregado exitosamente.")

        # Agregar 4 calificaciones para el nuevo curso a cada estudiante y actualizar el promedio
        for rut, datos in estudiantes_dict.items():
            calificaciones_curso = []
            for i in range(4):  # Pedir 4 notas
                while True:
                    try:
                        calificacion = float(input(f"Ingrese la calificación {i+1} en {nuevo_curso} para {datos['nombre']} (1-7): "))
                        if 1 <= calificacion <= 7:
                            calificaciones_curso.append(calificacion)
                            break
                        else:
                            print("La calificación debe estar entre 1 y 7.")
                    except ValueError:
                        print("Error: Ingrese un número válido.")
            
            # Agregar las 4 calificaciones del nuevo curso al diccionario del estudiante
            datos['calificaciones'].append(calificaciones_curso)

            # Recalcular el promedio general
            todas_las_notas = [nota for curso_notas in datos['calificaciones'] for nota in curso_notas]
            datos['promedio'] = sum(todas_las_notas) / len(todas_las_notas)
        print("Calificaciones actualizadas y promedios recalculados.")
    except Exception as e:
        print(f"Error al agregar curso: {e}")

def listar_cursos():
    print("\nLista de Cursos:")
    for i, curso in enumerate(cursos, start=1):
        print(f"{i}. {curso}")
    print("-" * 20)

def menu_cursos():
    while True:
        print("\nGestión de Cursos")
        print("1. Ver Calificaciones")
        print("2. Agregar Nuevo Curso")
        print("3. Listar Cursos")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        try:
            if opcion == '1':
                registrar_calificaciones()
            elif opcion == '2':
                agregar_curso()
            elif opcion == '3':
                listar_cursos()
            elif opcion == '4':
                break
            else:
                raise ValueError("Opción no válida. Intente de nuevo.")
        except ValueError as e:
            print(e)
