def main():
    # Crear el diccionario con los precios de las frutas
    precios_frutas = {
        "Pera": 0.85,
        "Manzana": 0.80,
        "Platano": 1.35,
        "Naranja": 0.70
    }

    # Mostrar el listado de frutas y precios
    print("Listado de frutas y sus precios (por kilo):")
    for fruta, precio in precios_frutas.items():
        print(f"{fruta}: ${precio:.2f} por kilo")

    # Pedir al usuario que introduzca una fruta y el número de kilos
    frutaInput = input("Introduce el nombre de la fruta: ").capitalize()
    kilos = float(input(f"¿Cuantos kilos de {frutaInput} quieres? "))

    # Verificar si la fruta está en el diccionario
    if frutaInput in precios_frutas:
        precio_total = precios_frutas[frutaInput] * kilos
        print(f"El precio de {kilos} kilos de {frutaInput} es ${precio_total:.2f}.")
    else:
        print(f"Lo siento, no tenemos {frutaInput} disponible.")

if __name__ == "__main__":
    main()
