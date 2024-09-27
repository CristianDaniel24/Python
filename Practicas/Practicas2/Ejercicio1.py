
def mostrarEstado(cobradas, pendientes):
    print(f"\nLa cantidad cobrada: {cobradas}")
    print(f"La cantidad pendiente de cobro: {sum(pendientes.values())}\n")

def agregarFactura(facturas):
    numero = input("Ingresa el numero de la nueva factura: ")
    valor = float(input("Ingresa el valor de la factura: "))
    facturas[numero] = valor
    print(f"La factura {numero} añadida con valor de {valor}.\n")

def pagarFactura(facturas, cobradas):
    numero = input("Introduce el numero de la factura para pagar: ")
    if numero in facturas:
        valor_pagado = facturas.pop(numero)
        cobradas += valor_pagado
        print(f"La factura {numero} pagada con valor de {valor_pagado}.\n")
    else:
        print(f"La factura {numero} no existe o es invalida\n")
    return cobradas

def main():
    facturas = {}  # Diccionario para almacenar las facturas
    cobradas = 0.0  # Suma de las facturas pagadas

    while True:
        print("1. Añadir factura nueva")
        print("2. Pagar factura existente")
        print("3. Salir")
        opcion = input("Ingresa una opcion:")

        if opcion == '1':
            agregarFactura(facturas)
        elif opcion == '2':
            cobradas = pagarFactura(facturas, cobradas)
        elif opcion == '3':
            print("Adios..")
            break
        else:
            print("Opcion invalida\n")

        mostrarEstado(cobradas, facturas)

if __name__ == "__main__":
    main()
