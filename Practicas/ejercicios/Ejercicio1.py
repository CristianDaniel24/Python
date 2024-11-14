
biblioteca = []
while True:
    try:
        print("\nMenu")
        print("1. Add")
        print("2. Delete")
        print("3. Search")
        print("4. Print list")
        print("5. Exit")
        opcion = int(input("Ingresa una opcion: "))
        if opcion == 1:
            while True:
                try:
                    titulo = " ".join(input("\nIngresa el nombre del libro: ").strip().split()).lower()
                    if not titulo:
                        raise ValueError ("El nombre del libro no puede estar vacío")

                    autor = " ".join(input("Ingrese el autor del libro: ").strip().split()).lower()
                    if not autor:
                        raise ValueError ("El nombre del autor no puede estar vacío")

                    ejemplares = int(input("Ingrese la cantidad de ejemplares: "))
                    if not ejemplares > 0:
                        raise ValueError ("La cantidad de ejemplares no puede estar vacía")

                    ejemplares = int(ejemplares)

                    libroEncontrado = False
                    for libro in biblioteca:
                        if libro[0] == titulo and libro[1] == autor:
                            libro[2] += ejemplares
                            libroEncontrado = True
                            print("\nEl libro ingresado ya existe")
                            print(f"Se ha actualizado la cantidad de {titulo} con un total de: {libro[2]}")
                            break
                    if not libroEncontrado:
                        biblioteca.append([titulo,autor,ejemplares])
                        print("\nSe ha agregado un nuevo libro con exito")
                    break
                except ValueError:
                    print("Error: Ingresa un número para la cantidad de ejemplares.")
        elif opcion == 2:
            if len(biblioteca) == 0:
                print("La biblioteca esta vacia no se puede eliminar nada")
            else:
                exit = True
                while exit:
                    print("\nMenu para eliminar libro")
                    print("1. Eliminar el libro totalmente")
                    print("2. Eliminar unicamente la cantidad del libro")
                    print("3. Exit")
                    opcionEliminar = int(input("Ingrese una opcion: "))
                    if opcionEliminar == 1:
                        print("\nIngresa el titulo y el autor del libro para eliminarlo totalmente")
                        tituloEliminar = input("Titulo del libro: ")
                        autorEliminar = input("Autor del libro: ")
                        for libro in biblioteca:
                            if libro[0] == tituloEliminar and libro[1] == autorEliminar:
                                print(f"El libro {libro[0]} ha sido eliminado con exito")
                                biblioteca.remove(libro)
                                exit = False
                            else:
                                print("\nEl libro no existe")
                                exit = False
                    elif opcionEliminar == 2:
                        print("\nIngresa el titulo, el autor y la cantidad del libro para eliminar la cantidad")
                        eliminarTitulo = input("Titulo del libro: ")
                        eliminarAutor = input("Autor del libro: ")
                        cantidadEliminar = int(input("Cantidad ha eliminar: "))
                        for libro in biblioteca:
                            if libro[0] == eliminarTitulo and libro[1] == eliminarAutor:
                                if cantidadEliminar > libro[2]:
                                    print(f"No se puede eliminar la cantidad del libro {libro[0]} porque hay unicamente {libro[2]} ejemplares")
                                    exit = False
                                else:
                                    libro[2] -= cantidadEliminar
                                    if libro[2] == 0:
                                        biblioteca.remove(libro)
                                        print(f"El libro {libro[0]} ha sido eliminado completamente porque hay 0 ejemplares")
                                        exit = False
                                    else:
                                        print(f"Al libro {libro[0]} se le han eliminado {cantidadEliminar} ejemplares, los ejemplares restantes son: {libro[2]}")
                                        exit = False
                            else:
                                print("\nEl libro no existe")
                                exit = False
                    elif opcionEliminar == 3:
                        exit = False
                    else:
                        print("La opcion es incorrecta")
        elif opcion == 3:
            if len(biblioteca) == 0:
                print("La biblioteca esta vacia no se puede buscar nada")
            else:
                libroBuscado = " ".join(input("\nIngrese el título del libro a buscar: ").strip().split()).lower()

                libroBuscadoEncontrado = False
                for libro in biblioteca:
                    if libro[0] == libroBuscado:
                        print(f"El libro {libroBuscado} si existe en la biblioteca")
                        libroBuscadoEncontrado = True

                if not libroBuscadoEncontrado:
                    print(f"El libro {libroBuscado} no se encontro en la biblioteca")

        elif opcion == 4:
            if len(biblioteca) == 0:
                print("La biblioteca esta vacia")
            else:
                print("\nEl contenido de la biblioteca es:")
                for libro in biblioteca:
                    print(f"Titulo: {libro[0]}, Autor: {libro[1]}, Ejemplares: {libro[2]}")
        elif opcion == 5:
            print("Exit..")
            break
        else:
            print("Opcion invalida")
    except ValueError:
        print("Ingresa un numero")
