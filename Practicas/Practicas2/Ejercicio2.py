
def main():
    # Crear el diccionario para almacenar la información del usuario
    usuario = {}

    # Pedir los datos del usuario
    usuario['nombre'] = input("Ingresa tu nombre: ")
    usuario['edad'] = input("Ingresa tu edad: ")
    usuario['direccion'] = input("Ingresa tu direccion: ")
    usuario['telefono'] = input("Ingresa tu numero de telefono: ")

    print(
        f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su numero de telefono es {usuario['telefono']}.")


if __name__ == "__main__":
    main()
