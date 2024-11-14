#Ingresar un numero por consola y los guarde y cuando ingrese un numero negativo
#imprima solo se permiten numero positivos

number = int(input("Enter the number:"))

if number >= 0:
    print("Correct, the number is positive")
else:
    print("Incorrect, the numer is negative")