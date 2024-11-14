number = 0

while(number < 3):
    try:
        print("\nMenu")
        print("1. Hacer suma")
        print("2. Salir")
        option = int(input("Ingrese una opcion: "))
        if option == 1:
            n1 = int(input("\nDigite el primer numero: "))
            n2 = int(input("Digite el segundo numero: "))
            operacion = n1 / n2
            print("El resultado es: ", operacion)
        elif option == 2:
            break
        else:
            print("Ingrese una opcion correcta")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        number += 1
    except ValueError:
        print("Ingrese un numero")
        number += 1