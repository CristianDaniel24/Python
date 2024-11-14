#Función que retorne el mayor de dos números o 0 si son iguales

def numElderly():
    num1 = int(input("Enter the number 1:\n"))
    num2 = int(input("Enter the number 2:\n"))

    if num1 > num2:
        print(f"The num elderly is: {num1}")
    elif num1 < num2:
        print(f"The num elderly is: {num2}")
    else:
        print("\n0")

numElderly()