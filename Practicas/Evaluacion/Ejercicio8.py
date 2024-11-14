#TODO: ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NUMERO ENTERO Y MUESTRE POR PANTALLA UN TRIANGULO RECTANGULO COMO EL DE MAS ABAJO
"""
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""
numberInput = int(input("Enter the number:"))

i = 0
for i in range(0, numberInput +1):
    i += 1
    print(f"{i}" * i)