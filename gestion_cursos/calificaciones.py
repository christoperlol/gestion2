from gestion_estudiante.gestion_estudiante import estudiantes_dict

# Se asume que la lista de cursos está definida y es accesible desde otro módulo.
cursos = ['modelamiento de datos', 'lenguaje programacion', 'ingles', 'taller de creatividad']

def registrar_calificaciones():
    try:
        if estudiantes_dict:
            print("\nCalificaciones por estudiante:")
            for rut, datos in estudiantes_dict.items():
                print(f"Estudiante: {datos['nombre']}")
                for i, curso in enumerate(cursos):
                    try:
                        nota = datos['calificaciones'][i]
                        print(f"  - {curso}: {nota}")
                    except IndexError:
                        print(f"  - {curso}: Sin calificación")
        else:
            print("No hay estudiantes registrados para mostrar calificaciones.")
    except Exception as e:
        print(f"Error al mostrar calificaciones: {e}")