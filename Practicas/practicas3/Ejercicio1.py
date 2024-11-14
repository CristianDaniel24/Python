
amount = int(input("Enter the amount for add to Set:"))

setNames = set()
setAges = set()

for i in range(amount):
    name = input("Enter the name:")
    setNames.add(name)

    age = int(input("Enter the age:"))
    setAges.add(age)

def filtrerAge(setNames, setAges):
    for names, age in zip(setNames,setAges):
        if age < 18:
            continue
        if age == 100:
            print(f"{names} tiene {age} años. Fin de la iteracion")
            break
        print(f"{names} tiene {age} años")

filtrerAge(setNames,setAges)
