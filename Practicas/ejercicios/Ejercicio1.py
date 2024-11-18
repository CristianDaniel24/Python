from xmlrpc.client import boolean


def agregarLibro():
    while True:
        try:
            titulo = " ".join(input("\nIngresa el nombre del libro: ").strip().split()).lower()
            if not titulo:
                raise ValueError("El nombre del libro no puede estar vacío")

            autor = " ".join(input("Ingrese el autor del libro: ").strip().split()).lower()
            if not autor:
                raise ValueError("El nombre del autor no puede estar vacío")

            ejemplares = int(input("Ingrese la cantidad de ejemplares: "))
            if not ejemplares > 0:
                raise ValueError("La cantidad de ejemplares no puede estar vacía")

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
                biblioteca.append([titulo, autor, ejemplares])
                print("\nSe ha agregado un nuevo libro con exito")
            break
        except ValueError:
            print("Error: Ingresa un número para la cantidad de ejemplares.")

def eliminarLibro():
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
                print(
                    "\nIngresa el titulo, el autor y la cantidad del libro para eliminar la cantidad")
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
                                print(
                                    f"El libro {libro[0]} ha sido eliminado completamente porque hay 0 ejemplares")
                                exit = False
                            else:
                                print(
                                    f"Al libro {libro[0]} se le han eliminado {cantidadEliminar} ejemplares, los ejemplares restantes son: {libro[2]}")
                                exit = False
                    else:
                        print("\nEl libro no existe")
                        exit = False
            elif opcionEliminar == 3:
                exit = False
            else:
                print("La opcion es incorrecta")

def buscarLibro():
    if len(biblioteca) == 0:
        print("La biblioteca esta vacia no se puede buscar nada")
    else:
        result = []
        libroBuscado = " ".join(input("\nIngrese el título del libro a buscar: ").strip().split()).lower()
        libroBuscadoEncontrado = False
        for libro in biblioteca:
            if libroBuscado in libro[0]:
                result.append(libro)
                libroBuscadoEncontrado = True

        if not libroBuscadoEncontrado:
            print(f"El libro {libroBuscado} no se encontro en la biblioteca")

        if libroBuscadoEncontrado:
            print("\nLos libros encontrados son:")
            for librosEncontrados in result:
                print(f"Titulo: {librosEncontrados[0]}, Autor: {librosEncontrados[1]}, Ejemplares: {librosEncontrados[2]}")

def buscarYEditarLibros():
    if len(biblioteca) == 0:
        print("La biblioteca esta vacia no se puede buscar nada")
    else:
        libroBuscado = " ".join(input("\nIngrese el título del libro a buscar: ").strip().split()).lower()

        #Es lo mismo del metodo de busqueda normal solo que en una linea
        result = [libro for libro in biblioteca if libroBuscado in libro[0]]
        if len(result) == 0:
            print(f"El libro {libroBuscado} no se encontro en la biblioteca")
            return
        exitModificacion = True
        while exitModificacion:
            if result:
                print("\nLos libros encontrados son:")
                for i, librosEncontrados in enumerate(result, start=1):
                    print(f"{i}. Titulo: {librosEncontrados[0]}, Autor: {librosEncontrados[1]}, Ejemplares: {librosEncontrados[2]}")

                seleccion = input("\nIngresa el numero del libro que deseas modificar: ")
                seleccion = int(seleccion) -1 #Se resta 1 porque los numeros mostrados al usuario comienzan desde 1, pero los indices en Python comienzan desde 0

                if 0 <= seleccion < len(result):
                    libro = result[seleccion]
                    print("\nEl libro seleccionado fue:")
                    print(f"Titulo: {libro[0]}, Autor: {libro[1]}, Ejemplares: {libro[2]}")

                    print("\nSelecciona que deseas modificar:")
                    print("1. Titulo")
                    print("2. Autor")
                    print("3. Ejemplares")
                    print("4. Exit")
                    opcion = int(input("Ingresa una opcion:"))

                    if opcion == 1:
                        nuevoTitulo = input("Ingresa el nuevo titulo del libro: ")
                        libro[0] = nuevoTitulo
                        print("El titulo ha sido modificado")
                        break
                    elif opcion == 2:
                        nuevoAutor = input("Ingresa el nuevo autor del libro: ")
                        libro[1] = nuevoAutor
                        print("El autor ha sido modificado")
                        break
                    elif opcion == 3:
                        nuevosEjemplares = int(input("Ingresa la los nuevos ejemplares del libro: "))
                        libro[3] = nuevosEjemplares
                        print("Los ejemplares del libro han sido modificados")
                        break
                    elif opcion == 4:
                        return
                    else:
                        print("La opcion es invalida")
                else:
                    print("La opcion es invalida")
def imprimirLibros():
    if len(biblioteca) == 0:
        print("La biblioteca esta vacia")
    else:
        print("\nEl contenido de la biblioteca es:")
        for libro in biblioteca:
            print(f"Titulo: {libro[0]}, Autor: {libro[1]}, Ejemplares: {libro[2]}")


biblioteca = []
while True:
    try:
        print("\nMenu")
        print("1. Add")
        print("2. Delete")
        print("3. Search")
        print("4. Search and edit")
        print("5. Print list")
        print("6. Exit")
        opcion = int(input("Ingresa una opcion: "))
        if opcion == 1:
            agregarLibro()
        elif opcion == 2:
            eliminarLibro()
        elif opcion == 3:
            buscarLibro()
        elif opcion == 4:
            buscarYEditarLibros()
        elif opcion == 5:
            imprimirLibros()
        elif opcion == 6:
            print("Exit..")
            break
        else:
            print("Opcion invalida")
    except ValueError:
        print("Ingresa un numero")
