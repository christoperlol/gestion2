
datos_universidad = {
    "nombre": "Universidad",
    "ubicacion": "Ciudad"
}

def menu_universidad():
    try:
        print("\nGestión de la Universidad")
        print(f"Nombre de la Universidad: {datos_universidad['nombre']}")
        print(f"Ubicación: {datos_universidad['ubicacion']}")
    except Exception as e:
        print(f"Error al mostrar la información de la universidad: {e}")
