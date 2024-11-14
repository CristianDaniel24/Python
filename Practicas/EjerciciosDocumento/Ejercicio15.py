

def ageTomorrow():
    listAgeTomorrow = []
    print("Enter the age of the Students of the tomorrow\n")
    for i in range(5):
        while True:
            try:
                age = int(input("Age tomorrow:"))
                listAgeTomorrow.append(age)
                break
            except ValueError:
                print("\nEnter the age, please\n")
    print("\nThe age of Tomorrow enters are:")
    print(listAgeTomorrow)
    avergeTomorrow(listAgeTomorrow)
    return listAgeTomorrow

def ageLate():
    listAgeLate = []
    print("\nEnter the age of the Students of the late\n")
    for i in range(6):
        while True:
            try:
                age = int(input("Age late:"))
                listAgeLate.append(age)
                break
            except ValueError:
                print("\nEnter the age, please\n")
    print("\nThe age of Late enters are:")
    print(listAgeLate)
    avergeLate(listAgeLate)
    return listAgeLate

def ageEvening():
    listAgeEvening = []
    print("\nEnter the age of the Students of the nigth\n")
    for i in range(11):
        while True:
            try:
                age = int(input("Age evening:"))
                listAgeEvening.append(age)
                break
            except ValueError:
                print("\nEnter the age, please\n")
    print("\nThe age of Evening enters are:")
    print(listAgeEvening)
    avergeEvening(listAgeEvening)
    return listAgeEvening

#PROMEDIOS
def avergeTomorrow(listAgeTomorrow):
    suma = sum(listAgeTomorrow)
    average = suma / len(listAgeTomorrow)
    print(f"\nThe average ages of the morning students are: {average}\n")
    return average

def avergeLate(listAgeLate):
    suma = sum(listAgeLate)
    average = suma / len(listAgeLate)
    print(f"\nThe average ages of the late students are: {average}\n")
    return average

def avergeEvening(listAgeEvening):
    suma = sum(listAgeEvening)
    average = suma / len(listAgeEvening)
    print(f"\nThe average ages of the evening students are: {average}\n")
    return average

def ageElderly():
    tomorrowAge = ageTomorrow()
    lateAge = ageLate()
    eveningAge = ageEvening()

    if tomorrowAge >= lateAge and tomorrowAge >= eveningAge:
        print(f"\nThe highest average is: {tomorrowAge}")
    elif lateAge >= tomorrowAge and lateAge >= eveningAge:
        print(f"\nThe highest average is: {lateAge}")
    else:
        print(f"\nThe highest average is: {eveningAge}")

#MENU
def menu():
    while True:
        print("\nWELCOME OF MENU!!")
        print("1. Enter the program")
        print("2. Exit")
        option = input("Enter the option\n")

        if option == "1":
            ageTomorrow()
            ageLate()
            ageEvening()
            ageElderly()
            break
        elif option == "2":
            print("\nExit..")
            break
        else:
            print("\nThe option is invalid")
if __name__ == "__main__":
    menu()