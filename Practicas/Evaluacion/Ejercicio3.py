"""
TODO: ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NUMERO ENTERO POSITIVO Y MUESTRE POR PANTALLA TODOS LOS NUMEROS IMPARES
TODO: DESDE 1 HASTA ESE NUMERO SEPARADOS POR COMAS
"""
number = int(input("Enter the number:"))

i = 0
while i < number:
    i += 1
    if i % 2 == 0:
        #NUMEROS PARES
        print()
    else:
        #NUMEROS IMPARES
        print(i,end = ",")
