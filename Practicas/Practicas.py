
suma = 0
while True:
    numero = int(input("Ingrse el numero: "))
    if numero == 0:
        print(f"The sum of numbers is: {suma}")
        break
    else:
        if numero % 2 == 0:
            suma += numero
        else:
            suma += numero