#Función que determine si una persona es mayor de edad o no (pista: el retorno debe ser un valor booleano)
def olderAge():
    age = int(input("Enter your age:"))
    adult = False

    if age >= 18:
        adult = True
    return adult


adult = olderAge()
if adult:
    print("You are older")
else:
    print("You are not old")